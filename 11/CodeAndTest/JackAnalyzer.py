import argparse
from asyncore import write
from glob import glob
import os
from msilib.schema import Directory
from symtable import SymbolTable
from textwrap import fill

class JackCompiler :
    def __init__(self, argString) :
        self.jackFileList = []
        self.outputFileList = []
        self.argString = argString


    def processFileName(self) :
        fileList = os.listdir(self.argString)
        for i in fileList :
            filename, fileExtension = os.path.splitext(self.argString + '/' + i)
            if fileExtension == '.jack' :
                self.jackFileList.append(filename + '.jack')
                self.outputFileList.append(filename + '.vm')

        print(f'jackFileList : {self.jackFileList}')
        print(f'outputFileList : {self.outputFileList}')

    def go(self) :
        self.processFileName()
        for i in range(len(self.jackFileList)) : 
            jt = JackTokenizer(self.jackFileList[i])
            CompilationEngine(self.outputFileList[i], jt)

            print(f"{self.jackFileList[i]} success")

            
    
# Ignores all comments and white space in the input stream, and serializes it intor
# Jack-language tokens. The token types are specified according to the Jack gramma
class JackTokenizer :
    def __init__(self, inputFileName) :
        self.currentToken = ''
        self.tokenType = ''

        # tokenType Ex : keyword, symbol, integerConstant, StringConstant, identifier, EOF, UNKNOWN
        with open(inputFileName, 'r') as f:
            self.data = f.read()

        ## Keyword Box ##
        self.keywordBox = ['class', 'constructor', 'function', 'method', 
            'field', 'static', 'var', 'int', 'char', 'boolean',
            'void', 'true', 'false', 'null', 'this', 'let', 'do', 
            'if', 'else', 'while', 'return']
        self.symbolBox = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+',
        '-', '*', '/', '&', '|', '<', '>', '=', '~']

        ## html code ##
        self.htmlBox = {'<' : '&lt;', '>' : '&gt;', '"' : '&quot;', '&' : '&amp;'}

    # lastChar funtion
    # string에서 읽어야하는 차례의 문자를 반환
    def lastChar(self) :
        if len(self.data) == len(self.currentToken) or self.currentToken == chr(26):
            return chr(26)              # EOF 문자
        return self.data[len(self.currentToken)]

    def hasMoreTokens(self) :
        self.currentToken = '' 

        self.data = self.data.lstrip()        # 공백, 주석 제거
        if self.data.startswith("//") :
            self.data = self.data.split('\n', maxsplit=1)[1] 
            return self.hasMoreTokens()
        if self.data.startswith("/**") :
            self.data = self.data.split('*/', maxsplit=1)[1]
            return self.hasMoreTokens()

        return self.lastChar() != chr(26)

    def advance(self) :
        if not self.hasMoreTokens() :
            return
        if self.lastChar().isalpha() or self.lastChar() == '_' :     # IDENT : [a-zA-Z_][a-zA-Z0-9_]*
            self.currentToken += self.lastChar()
            while self.lastChar().isalnum() or self.lastChar() == '_':
                self.currentToken += self.lastChar()

            if self.currentToken in self.keywordBox :
                self.tokenType = 'keyword'
            else :
                self.tokenType = 'identifier'

        elif self.lastChar().isdigit() :    # INT_LIT : [0-9]*
            self.currentToken += self.lastChar()
            while self.lastChar().isdigit() :
                self.currentToken += self.lastChar()
            self.tokenType = 'integerConstant'
        
        elif self.lastChar() == '"' :       # StringConstant : " ~ "
            self.currentToken += self.lastChar()
            while self.lastChar() != '"' :
                self.currentToken += self.lastChar() 
            self.currentToken += self.lastChar()
            self.tokenType = 'stringConstant'


        else :                      # else : EOF & MARK
            self.currentToken += self.lastChar()
            if self.currentToken == chr(26):   # 'EOF'
                self.currentToken = ''
                self.tokenType = 'EOF'
            elif self.currentToken in self.symbolBox :
                self.tokenType = 'symbol'
            else :                          # 'Else'
                self.tokenType = 'UNKNOWN'
                

        if self.tokenType != 'EOF' :
            self.data = self.data[len(self.currentToken):]

        if self.tokenType == 'stringConstant' :
            self.currentToken = self.currentToken[1:-1]
            self.currentToken.replace('\n', '')

        if self.currentToken in self.htmlBox :
            self.currentToken = self.htmlBox[self.currentToken]

    def writeOnFile(self, f) :
        f.write(f"<{self.tokenType}> ")
        f.write(self.currentToken)
        f.write(f" </{self.tokenType}>\n")

# Generates the compiler's output
class CompilationEngine :
    def __init__(self, outputFileName, jtt : JackTokenizer) :
        self.jt = jtt
        self.f = VMWriter(outputFileName)
        self.symbolTable = SymbolTable()

        self.className = ''
        self.counter = 0

        if self.jt.hasMoreTokens() :
            self.jt.advance()
            self.compileClass()
        else :
            print("error1")

    def __del__(self) :
        self.f.close()
        
    def compileClass(self) :
        self.f.write("<class>\n")
        if self.jt.currentToken == 'class' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.tokenType == 'identifier' :
                # self.jt.writeOnFile(self.f)
                self.className = self.jt.currentToken
                self.jt.advance()
                if self.jt.currentToken == '{' :
                    # self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    while self.jt.currentToken == 'static' or \
                            self.jt.currentToken == 'field' : 
                        self.compileClassVarDec()
                    while self.jt.currentToken == 'constructor' or \
                            self.jt.currentToken == 'function' or \
                            self.jt.currentToken == 'method' :
                        self.compileSubroutineDec()
                    if self.jt.currentToken == '}' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error2")
                else :
                    print("error3")
            else : 
                print(self.jt.currentToken)
        else :
            print("error4")
        self.f.write("</class> end\n")

    def compileClassVarDec(self) :
        varKind = ''
        varType = ''
        self.f.write("<classVarDec>\n")
        if self.jt.currentToken == 'static' or \
            self.jt.currentToken == 'field' :
            # self.jt.writeOnFile(self.f)
            varKind = self.jt.currentToken
            self.jt.advance()
            type = ['int', 'char', 'boolean']
            if self.jt.currentToken in type or \
                self.jt.tokenType == 'identifier' :
                # self.jt.writeOnFile(self.f)
                varType = self.jt.currentToken
                self.jt.advance()
                if self.jt.tokenType == 'identifier' :
                    # self.jt.writeOnFile(self.f)
                    self.symbolTable.define(self.jt.currentToken, varType, varKind)
                    self.jt.advance()
                else :
                    print("error5")
                while self.jt.currentToken == ',' :
                    # self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    if self.jt.tokenType == 'identifier' :
                        # self.jt.writeOnFile(self.f)
                        self.symbolTable.define(self.jt.currentToken, varType, varKind)
                        self.jt.advance()
                    else :
                        print("error6")
                if self.jt.currentToken == ';' :
                    # self.jt.writeOnFile(self.f)
                    self.jt.advance()
                else :
                    print("error7")
            else :
                print("error8")
        else :
            print("error9")
        self.f.write("</classVarDec> end\n") 

    def compileSubroutineDec(self) :
        subroutineName = ''
        whatType = ''

        self.f.write("<subroutineDec>\n")
        if self.jt.currentToken == 'constructor' or \
            self.jt.currentToken == 'function' or \
            self.jt.currentToken == 'method' :
            # self.jt.writeOnFile(self.f)
            whatType = self.jt.currentToken
            self.symbolTable.startSubroutine() 
            if self.jt.currentToken == 'method' :
                self.symbolTable.define('this', self.className, 'argument')
            self.jt.advance()
            type = ['void', 'int', 'char', 'boolean']
            if self.jt.currentToken in type or \
                self.jt.tokenType == 'identifier' :
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
                if self.jt.tokenType == 'identifier' :
                    # self.jt.writeOnFile(self.f)
                    subroutineName = self.jt.currentToken
                    self.jt.advance()
                    if self.jt.currentToken == '(' :
                        # self.jt.writeOnFile(self.f)
                        self.jt.advance()
                        self.compileParameterList()
                        if self.jt.currentToken == ')' :
                            # self.jt.writeOnFile(self.f)
                            
                            self.jt.advance()
                            self.compileSubroutineBody(subroutineName, whatType)
                        else :
                            print("error10")
                    else :
                        print("error11")
                   
                else :
                    print("error12")
            else :
                print("error13")
        self.f.write("</subroutineDec> end\n") 

    # parameterList : ((type varName) (',' type varName)*)?
    def compileParameterList(self) :
        tmpType = ''

        self.f.write("<parameterList>\n")
        type = ['int', 'char', 'boolean']
        if self.jt.currentToken in type or \
            self.jt.tokenType == 'identifier' :
            # self.jt.writeOnFile(self.f)
            tmpType = self.jt.currentToken
            self.jt.advance()
            if self.jt.tokenType == 'identifier' :
                # self.jt.writeOnFile(self.f)
                self.symbolTable.define(self.jt.currentToken, tmpType, 'argument')
                self.jt.advance()
                while self.jt.currentToken == ',' :
                    # self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    if self.jt.currentToken in type or \
                        self.jt.tokenType == 'identifier' :
                        # self.jt.writeOnFile(self.f)
                        tmpType = self.jt.currentToken
                        self.jt.advance()
                        if self.jt.tokenType == 'identifier' :
                            # self.jt.writeOnFile(self.f)
                            self.symbolTable.define(self.jt.currentToken, tmpType, 'argument')
                            self.jt.advance()
                        else :
                            print("error14")
                    else :
                        print("error15")
            else :
                print("error16")
        self.f.write("</parameterList> end\n")  

    # '{' varDec* statements '}'
    def compileSubroutineBody(self, subroutineName, whatType) :
        self.f.write("<subroutineBody>\n")
        if self.jt.currentToken == '{' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            while self.jt.currentToken == 'var' :
                self.compileVarDec()
            parameterCount = self.symbolTable.VarCount('local')
            self.f.writeFunction(f'{self.className}.{subroutineName}', parameterCount)
            if whatType == 'constructor' :
                self.f.writePush('constant', self.symbolTable.VarCount('field'))
                self.f.writeCall('Memory.alloc', 1)
                self.f.writePop('pointer', 0)
            elif whatType == 'method' :
                self.f.writePush('argument', 0)
                self.f.writePop('pointer', 0)
            self.compileStatements()
            if self.jt.currentToken == '}' :
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
            else :
                print("error17")
        else :
            print("error18")
        self.f.write("</subroutineBody> end\n")  

    # 'var' type varName (',' varName)* ';'
    def compileVarDec(self) :
        varType = ''

        self.f.write("<varDec>\n")
        if self.jt.currentToken == 'var' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            type = ['int', 'char', 'boolean']
            if self.jt.currentToken in type or \
                self.jt.tokenType == 'identifier' :
                # self.jt.writeOnFile(self.f)
                varType = self.jt.currentToken
                self.jt.advance()
                if self.jt.tokenType == 'identifier' :
                    # self.jt.writeOnFile(self.f)
                    self.symbolTable.define(self.jt.currentToken, varType, 'local')
                    self.jt.advance()
                    while self.jt.currentToken == ',' :
                        # self.jt.writeOnFile(self.f)
                        self.jt.advance()
                        if self.jt.tokenType == 'identifier' :
                            # self.jt.writeOnFile(self.f)
                            self.symbolTable.define(self.jt.currentToken, varType, 'local')
                            self.jt.advance()
                        else :
                            print("error19")
                    if self.jt.currentToken == ';' :
                        # self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error20")
                else :
                    print("error21")
            else :
                print("error22")
        else :
            print("error23")
        self.f.write("</varDec> end\n") 

    # statement*
    def compileStatements(self) :
        self.f.write("<statements>\n")
        while True :
            if self.jt.currentToken == 'let' :
                self.compileLet()
            elif self.jt.currentToken == 'if' :
                self.compileIf()
            elif self.jt.currentToken == 'while' :
                self.compileWhile()
            elif self.jt.currentToken == 'do' :
                self.compileDo()
            elif self.jt.currentToken == 'return' :
                self.compileReturn()
            else :
                break
        self.f.write("</statements> end\n") 

    # 'let' varName ('[' expression ']')? '=' exepression ';'
    def compileLet(self) :
        isArray = False
        varName = ''

        self.f.write("<letStatement>\n")
        if self.jt.currentToken == 'let' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.tokenType == 'identifier' :
                # self.jt.writeOnFile(self.f)
                varName = self.jt.currentToken
                self.jt.advance()
                if self.jt.currentToken == '[' :
                    # self.jt.writeOnFile(self.f)
                    isArray = True
                    self.jt.advance()
                    self.f.writePush(self.symbolTable.KindOf(varName),
                                        self.symbolTable.IndexOf(varName))
                    self.compileExpression()
                    self.f.writeArithmetic('add')
                    if self.jt.currentToken == ']' :
                        # self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error24")
                if self.jt.currentToken == '=' :
                    # self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    self.compileExpression()
                    if isArray :
                        self.f.writePop('temp', 0)

                        self.f.writePop('pointer', 1)
                        self.f.writePush('temp', 0)
                        self.f.writePop('that', 0)
                    else :
                        self.f.writePop(self.symbolTable.KindOf(varName),
                                        self.symbolTable.IndexOf(varName))
                        
                    if self.jt.currentToken == ';' :
                        # self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error25")
                else :
                    print("error26")
            else :
                print("error27")
        else :
            print("error28")
        self.f.write("</letStatement> end\n") 
 
    # 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
    def compileIf(self) :
        counter = self.counter
        self.counter += 1
        self.f.write("<ifStatement>\n")
        if self.jt.currentToken == 'if' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # (
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # expression
            self.compileExpression()
            self.f.writeIf(f'IF_TRUE{counter}')
            self.f.writeGoto(f'IF_FALSE{counter}')
            self.f.writeLabel(f'IF_TRUE{counter}')
            # )
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # {
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # statements
            self.compileStatements()
            
            # }
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.currentToken == 'else' :
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
                # {
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
                # statements
                self.f.writeGoto(f'IF_END{counter}')
                self.f.writeLabel(f'IF_FALSE{counter}')
                self.compileStatements()
                self.f.writeLabel(f'IF_END{counter}')
                # }
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
            else :
                self.f.writeLabel(f'IF_FALSE{counter}')
        else :
            print("error29")
        self.f.write("</ifStatement> end\n") 

    # 'while' '(' expression ')' '{' statements '}'
    def compileWhile(self) :
        counter = self.counter
        self.counter += 1
        self.f.write("<whileStatement>\n")
        if self.jt.currentToken == 'while' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # (
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # expression
            self.f.writeLabel(f'WHILE_EXP{counter}')
            self.compileExpression()
            self.f.writeArithmetic('not')
            self.f.writeIf(f'WHILE_END{counter}')
            # )
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # {
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # statements
            self.compileStatements()
            self.f.writeGoto(f'WHILE_EXP{counter}')
            self.f.writeLabel(f'WHILE_END{counter}')
            # }
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
        else :
            print("error30")
        self.f.write("</whileStatement> end\n")

    # 'do' subroutineCall ';'
    def compileDo(self) :
        subroutineName = ''
        nArgs = 0
        self.f.write("<doStatement>\n")
        if self.jt.currentToken == 'do' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            # subroutineCall
            # self.jt.writeOnFile(self.f)
            subroutineName += self.jt.currentToken
            self.jt.advance()
            if self.jt.currentToken == '.' :
                # self.jt.writeOnFile(self.f)
                if self.symbolTable.Typeof(subroutineName) != 'error' :
                    self.f.writePush(self.symbolTable.KindOf(subroutineName),
                                    self.symbolTable.IndexOf(subroutineName))
                    subroutineName = self.symbolTable.Typeof(subroutineName)
                    nArgs += 1
                subroutineName += self.jt.currentToken
                self.jt.advance()
                # 'subroutineName'
                # self.jt.writeOnFile(self.f)
                subroutineName += self.jt.currentToken
                self.jt.advance()
            if self.jt.currentToken == '(' :
                # self.jt.writeOnFile(self.f)
                if '.' not in subroutineName :
                    subroutineName = f'{self.className}.{subroutineName}'
                    nArgs += 1
                    self.f.writePush('pointer', 0)
                self.jt.advance()
                nArgs += self.compileExpressionList()
                self.f.writeCall(subroutineName, nArgs)
                self.f.writePop('temp', 0)
                # ')'
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
            else :
                print("error31")

            # subroutineCallEnd
            # ;
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
        else :
            print("error32")
        self.f.write("</doStatement> end\n")

    # 'return' expression? ';'
    def compileReturn(self) :
        self.f.write("<returnStatement>\n")
        # return
        # self.jt.writeOnFile(self.f)
        self.jt.advance()
        if self.jt.currentToken != ';' :
            self.compileExpression()
        else :
            self.f.writePush('constant', 0)
        self.f.writeReturn()
        # ;
        # self.jt.writeOnFile(self.f)
        self.jt.advance()
        self.f.write("</returnStatement> end\n")

    # term (op term)*
    # push something one
    def compileExpression(self) :
        whatOp = ''

        self.f.write("<expression>\n")
        self.compileTerm()
        op = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']
        opMap = {'+' : 'add', '-' : 'sub', '=' : 'eq', '&gt;' : 'gt',
                '&lt;' : 'lt', '&amp;' : 'and', '|' : 'or'}
        while self.jt.currentToken in op :
            # self.jt.writeOnFile(self.f)
            whatOp = self.jt.currentToken
            self.jt.advance()
            self.compileTerm()

            if whatOp in opMap :
                self.f.writeArithmetic(opMap[whatOp])
            elif whatOp == '*' :
                self.f.writeCall('Math.multiply', 2)
            elif whatOp == '/' :
                self.f.writeCall('Math.divide', 2)
            else :
                print(f"error34 {whatOp}")

        self.f.write("</expression>\n")

    # integerConstant | stringConstant | keywordConstant | varName |
    # varName '[' expression ']' | subroutineCall | '(' expression ')' |
    # unaryOp term
    # push something one
    def compileTerm(self) :
        varName = ''
        nArgs = 0
        whatUnaryOp = ''

        self.f.write(f"<term>\n")
        keywordConstant = {'true' : 0, 'false' : 0, 'null' : 0, 'this' : 'this'}
        unaryOp = {'-' : 'neg', '~' : 'not'}
        if self.jt.tokenType == 'integerConstant' or \
            self.jt.tokenType == 'stringConstant' or \
            self.jt.currentToken in keywordConstant :
            # self.jt.writeOnFile(self.f)
            if self.jt.currentToken == 'this' :
                self.f.writePush('pointer', 0)
            elif self.jt.currentToken in keywordConstant :
                self.f.writePush('constant', keywordConstant[self.jt.currentToken])
                if self.jt.currentToken == 'true' :
                    self.f.writeArithmetic('not')
            elif self.jt.tokenType == 'stringConstant' :
                targetString = self.jt.currentToken
                self.f.writePush('constant', len(targetString))
                self.f.writeCall('String.new', 1)
                for i in targetString :
                    self.f.writePush('constant', ord(i))
                    self.f.writeCall('String.appendChar', 2)
            else :
                self.f.writePush('constant', self.jt.currentToken)
            self.jt.advance()
        elif self.jt.currentToken == '(' :
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
            self.compileExpression()
            # ')'
            # self.jt.writeOnFile(self.f)
            self.jt.advance()
        elif self.jt.currentToken in unaryOp :
            # self.jt.writeOnFile(self.f)
            whatUnaryOp = unaryOp[self.jt.currentToken]
            self.jt.advance()
            self.compileTerm()
            self.f.writeArithmetic(whatUnaryOp)
            
        elif self.jt.tokenType == 'identifier' :
            # self.jt.writeOnFile(self.f)
            varName = self.jt.currentToken
            self.jt.advance()
            if self.jt.currentToken == '[' :
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.f.writePush(self.symbolTable.KindOf(varName),
                                self.symbolTable.IndexOf(varName))
                self.compileExpression()
                self.f.writeArithmetic('add')
                self.f.writePop('pointer', 1)
                self.f.writePush('that', 0)
                # ']'
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
            elif self.jt.currentToken == '(' :
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
                nArgs = self.compileExpressionList()
                self.f.writePush('pointer', 0)
                self.f.writeCall(f'{self.className}.{varName}', nArgs + 1)
                # ')'
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
            elif self.jt.currentToken == '.' :
                # self.jt.writeOnFile(self.f)
                if self.symbolTable.Typeof(varName) != 'error' :
                    self.f.writePush(self.symbolTable.KindOf(varName),
                                    self.symbolTable.IndexOf(varName))
                    varName = self.symbolTable.Typeof(varName)
                    nArgs += 1
                varName += self.jt.currentToken
                self.jt.advance()
                # 'subroutineName'
                # self.jt.writeOnFile(self.f)
                varName += self.jt.currentToken
                self.jt.advance()
                # '('
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
                nArgs += self.compileExpressionList()
                self.f.writeCall(varName, nArgs)
                # ')'
                # self.jt.writeOnFile(self.f)
                self.jt.advance()
            else :
                self.f.writePush(self.symbolTable.KindOf(varName),
                                self.symbolTable.IndexOf(varName))
        else :
            print("error33")    
        self.f.write("</term> end\n")

    # (expression (',' expression)*)?
    def compileExpressionList(self) :
        nArgs = 0

        self.f.write("<expressionList>\n")
        keywordConstant = ['true', 'false', 'null', 'this']
        unaryOp = ['-', '~']
        if self.jt.tokenType == 'integerConstant' or \
            self.jt.tokenType == 'stringConstant' or \
            self.jt.currentToken in keywordConstant or \
            self.jt.currentToken == '(' or \
            self.jt.currentToken in unaryOp or \
            self.jt.tokenType == 'identifier' :
            nArgs += 1
            self.compileExpression()
            while self.jt.currentToken == ',' :
                # self.jt.writeOnFile(self.f)
                nArgs += 1
                self.jt.advance()
                self.compileExpression()
        self.f.write("</expressionList>\n")

        return nArgs

class SymbolTable :
    def __init__(self) :
        # name : [type, kind, #] 형식으로
        # type ex : int, float, Point ...
        # kind ex : STATIC, FIELD, ARG, VAR
        self.baseSym = {}  
        self.subSym = {}
        self.kindCount = {'static' : 0, 'field' : 0, 'argument' : 0, 'local' : 0}     # kind 나타난 수

    def startSubroutine(self) :
        self.subSym = {}
        self.kindCount['argument'] = 0
        self.kindCount['local'] = 0

    def define(self, name, ttype, kind) :
        if kind == 'static' or kind == 'field':
            self.baseSym[name] = [ttype, kind, self.kindCount[kind]]
            self.kindCount[kind] += 1

        elif kind == 'argument' or kind == 'local':
            self.subSym[name] = [ttype, kind, self.kindCount[kind]]
            print(self.subSym)
            self.kindCount[kind] += 1
    
    
    def VarCount(self, kind) :
        return self.kindCount[kind]

    def KindOf(self, name) :
        if name in self.subSym :
            return self.subSym[name][1]
        elif name in self.baseSym :
            return self.baseSym[name][1]
        else :
            return 'error'

    def Typeof(self, name) :
        if name in self.subSym :
            return self.subSym[name][0]
        elif name in self.baseSym :
            return self.baseSym[name][0]
        else :
            return 'error'

    def IndexOf(self, name) :
        if name in self.subSym :
            return self.subSym[name][2]
        elif name in self.baseSym :
            return self.baseSym[name][2]
        else :
            return -1
        
class VMWriter :
    def __init__(self, outputFileName) :
        self.f = open(outputFileName, 'w')

    def write(self, tmp) :
        # self.f.write(tmp)
        return

    # segment : const, argument, local, static, this, that, pointer, temp
    def writePush(self, segment, index) :
        if segment == 'field' :
            segment = 'this'
        self.f.write(f'push {segment} {index}\n')

    # segment : const, arg, local, static, this, that, pointer, temp
    def writePop(self, segment, index) :
        if segment == 'field' :
            segment = 'this'
        self.f.write(f'pop {segment} {index}\n')

    # command : add, sub, neg, eq, gt, lt, and, or, not
    def writeArithmetic(self, command) :
        self.f.write(command + '\n')

    def writeLabel(self, label) :
        self.f.write(f'label {label}\n')

    def writeGoto(self, label) :
        self.f.write(f'goto {label}\n')

    def writeIf(self, label) :
        self.f.write(f'if-goto {label}\n')

    def writeCall(self, name, nArgs) :
        self.f.write(f'call {name} {nArgs}\n')

    def writeFunction(self, name, nLocals) :
        self.f.write(f'function {name} {nLocals}\n')

    def writeReturn(self) :
        self.f.write('return\n')

    def close(self) :
        self.f.close()

# drives the process
def main() :
    argTool = argparse.ArgumentParser()
    argTool.add_argument('directoryName', type=str, help="Enter directory name")
    args = argTool.parse_args()
    args = args.directoryName
    jackcompiler = JackCompiler(args)
    jackcompiler.go()
    


if __name__=="__main__":
    main()