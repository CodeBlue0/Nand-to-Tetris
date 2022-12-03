import argparse
from asyncore import write
from glob import glob
import os
from msilib.schema import Directory
from symtable import SymbolTable
from textwrap import fill

class JackAnalyzer :
    def __init__(self, argString) :
        self.jackFileList = []
        self.outputFileTList = []
        self.outputFileList = []
        self.argString = argString


    def processFileName(self) :
        fileList = os.listdir(self.argString)
        for i in fileList :
            filename, fileExtension = os.path.splitext(self.argString + '/' + i)
            if fileExtension == '.jack' :
                self.jackFileList.append(filename + '.jack')
                self.outputFileList.append(filename + '.xml')
                self.outputFileTList.append(filename + 'T.xml')

        print(f'jackFileList : {self.jackFileList}')
        print(f'outputFileList : {self.outputFileList}')
        print(f'outputFileTList : {self.outputFileTList}')

    def go(self) :
        self.processFileName()
        for i in range(len(self.jackFileList)) : 
            jt = JackTokenizer(self.jackFileList[i])

            with open(self.outputFileTList[i], 'w') as f :
                f.write("<tokens>\n")
                while jt.hasMoreTokens() :
                    jt.advance()
                    jt.writeOnFile(f)
                f.write("</tokens>")
            jt = JackTokenizer(self.jackFileList[i])
            CompilationEngine(self.outputFileList[i], jt)

            print(f"{self.jackFileList[i]} success")

            
    
# Ignores all comments and white space in the input stream, and serializes it intor
# Jack-language tokens. The token types are specified according to the Jack gramma
class JackTokenizer :
    def __init__(self, inputFileName) :
        self.currentToken = ''
        self.tokenType = ''
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
        self.f = open(outputFileName, 'w')
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
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.tokenType == 'identifier' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                if self.jt.currentToken == '{' :
                    self.jt.writeOnFile(self.f)
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
        self.f.write("</class>\n")

    def compileClassVarDec(self) :
        self.f.write("<classVarDec>\n")
        if self.jt.currentToken == 'static' or \
            self.jt.currentToken == 'field' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            type = ['int', 'char', 'boolean']
            if self.jt.currentToken in type or \
                self.jt.tokenType == 'identifier' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                if self.jt.tokenType == 'identifier' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                else :
                    print("error5")
                while self.jt.currentToken == ',' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    if self.jt.tokenType == 'identifier' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error6")
                if self.jt.currentToken == ';' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                else :
                    print("error7")
            else :
                print("error8")
        else :
            print("error9")
        self.f.write("</classVarDec>\n") 

    def compileSubroutineDec(self) :
        self.f.write("<subroutineDec>\n")
        if self.jt.currentToken == 'constructor' or \
            self.jt.currentToken == 'function' or \
            self.jt.currentToken == 'method' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            type = ['void', 'int', 'char', 'boolean']
            if self.jt.currentToken in type or \
                self.jt.tokenType == 'identifier' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                if self.jt.tokenType == 'identifier' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    if self.jt.currentToken == '(' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                        self.compileParameterList()
                        if self.jt.currentToken == ')' :
                            self.jt.writeOnFile(self.f)
                            self.jt.advance()
                            self.compileSubroutineBody()
                        else :
                            print("error10")
                    else :
                        print("error11")
                   
                else :
                    print("error12")
            else :
                print("error13")
        self.f.write("</subroutineDec>\n") 

    # parameterList : ((type varName) (',' type varName)*)?
    def compileParameterList(self) :
        self.f.write("<parameterList>\n")
        type = ['int', 'char', 'boolean']
        if self.jt.currentToken in type or \
            self.jt.tokenType == 'identifier' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.tokenType == 'identifier' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                while self.jt.currentToken == ',' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    if self.jt.currentToken in type or \
                        self.jt.tokenType == 'identifier' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                        if self.jt.tokenType == 'identifier' :
                            self.jt.writeOnFile(self.f)
                            self.jt.advance()
                        else :
                            print("error14")
                    else :
                        print("error15")
            else :
                print("error16")
        self.f.write("</parameterList>\n")  

    # '{' varDec* statements '}'
    def compileSubroutineBody(self) :
        self.f.write("<subroutineBody>\n")
        if self.jt.currentToken == '{' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            while self.jt.currentToken == 'var' :
                self.compileVarDec()
            self.compileStatements()
            if self.jt.currentToken == '}' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
            else :
                print("error17")
        else :
            print("error18")
        self.f.write("</subroutineBody>\n")  

    # 'var' type varName (',' varName)* ';'
    def compileVarDec(self) :
        self.f.write("<varDec>\n")
        if self.jt.currentToken == 'var' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            type = ['int', 'char', 'boolean']
            if self.jt.currentToken in type or \
                self.jt.tokenType == 'identifier' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                if self.jt.tokenType == 'identifier' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    while self.jt.currentToken == ',' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                        if self.jt.tokenType == 'identifier' :
                            self.jt.writeOnFile(self.f)
                            self.jt.advance()
                        else :
                            print("error19")
                    if self.jt.currentToken == ';' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error20")
                else :
                    print("error21")
            else :
                print("error22")
        else :
            print("error23")
        self.f.write("</varDec>\n") 

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
        self.f.write("</statements>\n") 

    # 'let' varName ('[' expression ']')? '=' exepression ';'
    def compileLet(self) :
        self.f.write("<letStatement>\n")
        if self.jt.currentToken == 'let' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.tokenType == 'identifier' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                if self.jt.currentToken == '[' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    self.compileExpression()
                    if self.jt.currentToken == ']' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error24")
                if self.jt.currentToken == '=' :
                    self.jt.writeOnFile(self.f)
                    self.jt.advance()
                    self.compileExpression()
                    if self.jt.currentToken == ';' :
                        self.jt.writeOnFile(self.f)
                        self.jt.advance()
                    else :
                        print("error25")
                else :
                    print("error26")
            else :
                print("error27")
        else :
            print("error28")
        self.f.write("</letStatement>\n") 
 
    # 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
    def compileIf(self) :
        self.f.write("<ifStatement>\n")
        if self.jt.currentToken == 'if' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # (
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # expression
            self.compileExpression()
            # )
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # {
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # statements
            self.compileStatements()
            # }
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.currentToken == 'else' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                # {
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                # statements
                self.compileStatements()
                # }
                self.jt.writeOnFile(self.f)
                self.jt.advance()
        else :
            print("error29")
        self.f.write("</ifStatement>\n") 

    # 'while' '(' expression ')' '{' statements '}'
    def compileWhile(self) :
        self.f.write("<whileStatement>\n")
        if self.jt.currentToken == 'while' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # (
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # expression
            self.compileExpression()
            # )
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # {
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # statements
            self.compileStatements()
            # }
            self.jt.writeOnFile(self.f)
            self.jt.advance()
        else :
            print("error30")
        self.f.write("</whileStatement>\n")

    # 'do' subroutineCall ';'
    def compileDo(self) :
        self.f.write("<doStatement>\n")
        if self.jt.currentToken == 'do' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            # subroutineCall
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.currentToken == '(' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.compileExpressionList()
                # ')'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
            elif self.jt.currentToken == '.' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                # 'subroutineName'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                # '('
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.compileExpressionList()
                # ')'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
            else :
                print("error31")

            # subroutineCallEnd
            # ;
            self.jt.writeOnFile(self.f)
            self.jt.advance()
        else :
            print("error32")
        self.f.write("</doStatement>\n")

    # 'return' expression? ';'
    def compileReturn(self) :
        self.f.write("<returnStatement>\n")
        # return
        self.jt.writeOnFile(self.f)
        self.jt.advance()
        if self.jt.currentToken != ';' :
            self.compileExpression()
        # ;
        self.jt.writeOnFile(self.f)
        self.jt.advance()
        self.f.write("</returnStatement>\n")

    # term (op term)*
    def compileExpression(self) :
        self.f.write("<expression>\n")
        self.compileTerm()
        op = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']
        while self.jt.currentToken in op :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            self.compileTerm()
        self.f.write("</expression>\n")

    # integerConstant | stringConstant | keywordConstant | varName |
    # varName '[' expression ']' | subroutineCall | '(' expression ')' |
    # unaryOp term
    def compileTerm(self) :
        self.f.write(f"<term>\n")
        keywordConstant = ['true', 'false', 'null', 'this']
        unaryOp = ['-', '~']
        if self.jt.tokenType == 'integerConstant' or \
            self.jt.tokenType == 'stringConstant' or \
            self.jt.currentToken in keywordConstant :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
        elif self.jt.currentToken == '(' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            self.compileExpression()
            # ')'
            self.jt.writeOnFile(self.f)
            self.jt.advance()
        elif self.jt.currentToken in unaryOp :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            self.compileTerm()
        elif self.jt.tokenType == 'identifier' :
            self.jt.writeOnFile(self.f)
            self.jt.advance()
            if self.jt.currentToken == '[' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.compileExpression()
                # ']'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
            elif self.jt.currentToken == '(' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.compileExpressionList()
                # ')'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
            elif self.jt.currentToken == '.' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                # 'subroutineName'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                # '('
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.compileExpressionList()
                # ')'
                self.jt.writeOnFile(self.f)
                self.jt.advance()
        else :
            print("error33")    
        self.f.write("</term>\n")

    # (expression (',' expression)*)?
    def compileExpressionList(self) :
        self.f.write("<expressionList>\n")
        keywordConstant = ['true', 'false', 'null', 'this']
        unaryOp = ['-', '~']
        if self.jt.tokenType == 'integerConstant' or \
            self.jt.tokenType == 'stringConstant' or \
            self.jt.currentToken in keywordConstant or \
            self.jt.currentToken == '(' or \
            self.jt.currentToken in unaryOp or \
            self.jt.tokenType == 'identifier' :
            self.compileExpression()
            while self.jt.currentToken == ',' :
                self.jt.writeOnFile(self.f)
                self.jt.advance()
                self.compileExpression()
        self.f.write("</expressionList>\n")

# drives the process
def main() :
    argTool = argparse.ArgumentParser()
    argTool.add_argument('directoryName', type=str, help="Enter directory name")
    args = argTool.parse_args()
    args = args.directoryName
    jackanalyzer = JackAnalyzer(args)
    jackanalyzer.go()
    


if __name__=="__main__":
    main()