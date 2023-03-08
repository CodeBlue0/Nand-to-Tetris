fileName = 'StaticTest'
inputFileName = fileName + '.vm'
outputFileName = fileName + '.asm'

COMMANDTYPE = {
    'C_ARITHMETIC':1,
    'C_PUSH':2,
    'C_POP':3,
    'C_LABEL':4,
    'C_GOTO':5,
    'C_IT':6,
    'C_FUNCTION':7,
    'C_RETURN':8,
    'C_CALL':9
}

ARITHMETIC_LOGICAL_CAMMANDS = ['add','sub','neg','eq','gt','lt','and','or','not']

# parses each VM command into its lexical elements
class Parser :
    def __init__(self) :
        self.line = ''      # 현재의 line
        self.type = 0       # line의 종류 (in COMMANDTYPE)
        self.arg1 = ''      # 파라미터1 (연산자의 유형 / 메모리 종류)
        self.arg2 = 0       # 파라미터2 (메모리 위치)
        self.f = open(inputFileName, 'r')

    def __del__(self) :
        self.f.close()

    def readOneLine(self) :
        tmpLine = self.f.readline()
        if not tmpLine :
            return -1

        tmpLine = tmpLine.split('/', maxsplit=2)[0]    # 주석제거
        tmpLine = tmpLine.strip()                      # 앞 뒤 공백 제거
        if len(tmpLine) == 0 :                         # 빈 문자열 제거
            return self.readOneLine()
            
        print(tmpLine)                                  # line 출력
        self.line = tmpLine                         
        return 0             

    def parser(self) :
        if self.readOneLine() == -1:
            return -1

        lineDetail = self.line.split(' ', maxsplit=3)
        if lineDetail[0] in ARITHMETIC_LOGICAL_CAMMANDS :
            self.type = COMMANDTYPE['C_ARITHMETIC']
            self.arg1 = lineDetail[0]
        elif lineDetail[0] == 'push' :
            self.type = COMMANDTYPE['C_PUSH']
            self.arg1 = lineDetail[1]
            self.arg2 = lineDetail[2]
        elif lineDetail[0] == 'pop' :
            self.type = COMMANDTYPE['C_POP']
            self.arg1 = lineDetail[1]
            self.arg2 = lineDetail[2]

        

# writes the assembly code that implements the parsed command 
class CodeWriter :
    def __init__(self) :
        self.BASEADDTABLE = {
            'local':'LCL',
            'argument':'ARG',
            'this':'THIS',
            'that':'THAT'
        }
        self.setBranchIndex = 0
        self.f = open(outputFileName, 'w')

    def __del__(self) :
        self.f.close()

    def writeArithmetic(self, command) :

        hackCode = f"// {command}\n"

        if command == 'neg' or command == 'not':
            hackCode += f'@SP\n'
            hackCode += f'A=M-1\n'
            if command == 'neg' :
                hackCode += f'M=-M\n'
            elif command == 'not' :
                hackCode += f'M=!M\n'

        else :
            hackCode += f'@SP\n'    
            hackCode += f'A=M-1\n'  
            hackCode += f'D=M\n'      
            hackCode += f'A=A-1\n' 

            if command == 'add' :   
                hackCode += f'M=D+M\n'
            elif command == 'sub' :
                hackCode += f'M=M-D\n'
            elif command == 'and' :
                hackCode += f'M=D&M\n'
            elif command == 'or' :
                hackCode += f'M=D|M\n'
            else :
                hackCode += f'D=M-D\n'
                hackCode += f'@SETTRUE{self.setBranchIndex}\n'
                if command == 'eq' :
                    hackCode += f'D;JEQ\n'
                elif command == 'gt' :
                    hackCode += f'D;JGT\n'
                elif command == 'lt' :
                    hackCode += f'D;JLT\n'
                hackCode += f'@SP\n'
                hackCode += f'A=M-1\n'
                hackCode += f'A=A-1\n'
                hackCode += f'M=0\n'
                hackCode += f'@END{self.setBranchIndex}\n'
                hackCode += f'0;JMP\n'
                hackCode += f'(SETTRUE{self.setBranchIndex})\n'
                hackCode += f'@SP\n'
                hackCode += f'A=M-1\n'
                hackCode += f'A=A-1\n'
                hackCode += f'M=-1\n'
                hackCode += f'@END{self.setBranchIndex}\n'
                hackCode += f'0;JMP\n'
                hackCode += f'(END{self.setBranchIndex})\n'
                self.setBranchIndex += 1

            hackCode += f'@SP\n'
            hackCode += f'M=M-1\n'

        self.f.write(hackCode)
    
    def writePushPop(self, commandType, segment, index) :

        hackCode = f"// {('push' if commandType == 2 else 'pop')} {segment} {index}\n"

        if commandType == COMMANDTYPE['C_PUSH'] :
            hackCode += f'// get {segment} {index}\n'
            if segment == 'constant' :                  # constant
                hackCode += f'@{str(index)}\n'
                hackCode += f'D=A\n'
            elif segment in self.BASEADDTABLE.keys() :  # local, argument, this, that
                hackCode += f'@{index}\n'
                hackCode += f'D=A\n' 
                hackCode += f'@{self.BASEADDTABLE[segment]}\n'
                hackCode += f'A=D+M\n'
                hackCode += f'D=M\n'
            elif segment == 'temp' :                    # temp
                hackCode += f'@{index}\n'
                hackCode += f'D=A\n' 
                hackCode += f'@5\n'
                hackCode += f'A=D+A\n'
                hackCode += f'D=M\n'
            elif segment == 'pointer' :                 # pointer
                hackCode += f'@{index}\n'
                hackCode += f'D=A\n' 
                hackCode += f'@3\n'
                hackCode += f'A=D+A\n'
                hackCode += f'D=M\n'        
            elif segment == 'static' :
                hackCode += f'@{fileName}.{index}\n'
                hackCode += f'D=M\n'

            hackCode += '// push to stack\n'
            hackCode += '@SP\n'
            hackCode += 'A=M\n'
            hackCode += 'M=D\n'
            hackCode += '@SP\n'
            hackCode += 'M=M+1\n'

        elif commandType == COMMANDTYPE['C_POP'] :
            hackCode += '// pop from stack\n'
            hackCode += '@SP\n'
            hackCode += 'M=M-1\n'
            hackCode += '@SP\n'
            hackCode += 'A=M\n'
            hackCode += 'D=M\n'
            hackCode += f'@popTmp\n'    # popTmp1: 스택의 값 저장
            hackCode += f'M=D\n'

            hackCode += f'// put {segment} {index}\n'
            if segment in self.BASEADDTABLE.keys() :    # local, argument, this, that
                hackCode += f'@{index}\n'
                hackCode += f'D=A\n' 
                hackCode += f'@{self.BASEADDTABLE[segment]}\n'
                hackCode += f'D=D+M\n'
            elif segment == 'temp' :                    # temp
                hackCode += f'@{index}\n'
                hackCode += f'D=A\n' 
                hackCode += f'@5\n'
                hackCode += f'D=D+A\n'
            elif segment == 'pointer' :                 # pointer
                hackCode += f'@{index}\n'
                hackCode += f'D=A\n' 
                hackCode += f'@3\n'
                hackCode += f'D=D+A\n'
            elif segment == 'static' :                  # static
                hackCode += f'@{fileName}.{index}\n'
                hackCode += f'D=A\n' 

            hackCode += f'@popTmp2\n'   # popTmp2: 저장 목표 장소의 주소 저장
            hackCode += f'M=D\n'

            hackCode += f'@popTmp\n'
            hackCode += f'D=M\n'

            hackCode += f'@popTmp2\n'
            hackCode += f'A=M\n'
            hackCode += f'M=D\n'


        self.f.write(hackCode)

# drives the process
def main() :
    parser = Parser()
    codeWriter = CodeWriter()
    while True :
        if parser.parser() == -1:
            break
        if parser.type == COMMANDTYPE['C_ARITHMETIC'] :
            codeWriter.writeArithmetic(parser.arg1)
        elif parser.type == COMMANDTYPE['C_POP'] \
            or parser.type == COMMANDTYPE['C_PUSH'] :
            codeWriter.writePushPop(parser.type, parser.arg1, parser.arg2)
        
        print(f'종류: {parser.type}, 파라미터 {parser.arg1} {parser.arg2}')
            
if __name__=="__main__":
    main()