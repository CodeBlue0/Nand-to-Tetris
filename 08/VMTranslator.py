import argparse
from asyncore import write
from glob import glob
import os
from msilib.schema import Directory
from symtable import SymbolTable
from textwrap import fill

vmFileList = []
targetDirectory = ''
inputFileName = '' + '.vm'
outputFileName = '' + '.asm'

COMMANDTYPE = {
    'C_ARITHMETIC':1,
    'C_PUSH':2,
    'C_POP':3,
    'C_LABEL':4,
    'C_GOTO':5,
    'C_IF':6,
    'C_FUNCTION':7,
    'C_CALL':8,
    'C_RETURN':9,

}

ARITHMETIC_LOGICAL_CAMMANDS = ['add','sub','neg','eq','gt','lt','and','or','not']

# parses each VM command into its lexical elements
class Parser :
    def __init__(self) :
        global targetDirectory
        global inputFileName

        self.line = ''      # 현재의 line
        self.type = 0       # line의 종류 (in COMMANDTYPE)
        self.arg1 = ''      # 파라미터1 (연산자의 유형 / 메모리 종류)
        self.arg2 = 0       # 파라미터2 (메모리 위치)
        self.f = open(targetDirectory + '/' + inputFileName, 'r')

    def __del__(self) :
        self.f.close()

    def readOneLine(self, codewriter) :
        tmpLine = self.f.readline()
        if not tmpLine :
            return -1

        tmpLine = tmpLine.split('/', maxsplit=1)    # 주석제거
        if len(tmpLine) == 2 :
            codewriter.f.write('// /' + tmpLine[1])
        tmpLine = tmpLine[0]
        tmpLine = tmpLine.strip()                      # 앞 뒤 공백 제거
        if len(tmpLine) == 0 :                         # 빈 문자열 제거
            return self.readOneLine(codewriter)
            
        print(tmpLine)                                  # line 출력
        self.line = tmpLine                         
        return 0             

    def parser(self, codewriter) :
        if self.readOneLine(codewriter) == -1:
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
        elif lineDetail[0] == 'label' :
            self.type = COMMANDTYPE['C_LABEL']
            self.arg1 = lineDetail[1]
        elif lineDetail[0] == 'goto' :
            self.type = COMMANDTYPE['C_GOTO']
            self.arg1 = lineDetail[1]
        elif lineDetail[0] == 'if-goto' :
            self.type = COMMANDTYPE['C_IF']
            self.arg1 = lineDetail[1]
        elif lineDetail[0] == 'function' :
            self.type = COMMANDTYPE['C_FUNCTION']
            self.arg1 = lineDetail[1]
            self.arg2 = lineDetail[2]
        elif lineDetail[0] == 'call' :
            self.type = COMMANDTYPE['C_CALL']
            self.arg1 = lineDetail[1]
            self.arg2 = lineDetail[2]
        elif lineDetail[0] == 'return' :
            self.type = COMMANDTYPE['C_RETURN']


        

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
        self.returnAddressIndex = 1
        self.f = open(targetDirectory + '/' + outputFileName, 'w')
        self.writeInit()

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

        if commandType == COMMANDTYPE['C_PUSH'] :
            hackCode = f'// get {segment} {index}\n'
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
                hackCode += f'@{inputFileName[:-3]}.{index}\n'
                hackCode += f'D=M\n'
            elif segment == 'var' :                     # 추가 function call 기능을 위해 branch 추가
                hackCode += f'@{str(index)}\n'
                hackCode += f'D=M\n'

            hackCode += '// push to stack\n'
            hackCode += '@SP\n'
            hackCode += 'A=M\n'
            hackCode += 'M=D\n'
            hackCode += '@SP\n'
            hackCode += 'M=M+1\n'

        elif commandType == COMMANDTYPE['C_POP'] :
            hackCode = '// pop from stack\n'
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
                hackCode += f'@{inputFileName[:-3]}.{index}\n'
                hackCode += f'D=A\n' 
            elif segment == 'var' :                     # 추가 function call 기능을 위해 branch 추가
                hackCode += f'@{str(index)}\n'
                hackCode += f'D=A\n'

            hackCode += f'@popTmp2\n'   # popTmp2: 저장 목표 장소의 주소 저장
            hackCode += f'M=D\n'

            hackCode += f'@popTmp\n'
            hackCode += f'D=M\n'

            hackCode += f'@popTmp2\n'
            hackCode += f'A=M\n'
            hackCode += f'M=D\n'


        self.f.write(hackCode)

    def writeInit(self) :
        hackCode = f'// Bootstrap\n'
        hackCode += f'@256\n'
        hackCode += f'D=A\n'
        hackCode += f'@SP\n'
        hackCode += f'M=D\n'
        hackCode += f'@0\n'
        hackCode += f'D=A\n'
        inputTmpSegment = ['LCL', 'ARG', 'THIS', 'THAT']
        for i in inputTmpSegment :
            hackCode += f'D=D-1\n'
            hackCode += f'@{i}\n'
            hackCode += f'M=D\n'
        
        self.f.write(hackCode)
        self.writeCall('Sys.init', 0)

    def writeLabel(self, label) :
        hackCode = f'// define label\n'
        hackCode += f'({label})\n'
        self.f.write(hackCode)

    def writeGoto(self, label) :
        hackCode = f'// goto command\n'
        hackCode += f'@{label}\n'
        hackCode += f'0;JMP\n'
        self.f.write(hackCode)

    def writeIf(self, label) :
        hackCode = '// if-goto command\n'
        hackCode += '// pop from stack\n'
        hackCode += '@SP\n'
        hackCode += 'M=M-1\n'
        hackCode += 'A=M\n'
        hackCode += 'D=M\n'
        hackCode += f'@{label}\n'
        hackCode += f'D;JNE\n'
        self.f.write(hackCode)
        
    # localNum번 push 0을 수행 
    def writeFunction(self, name, localNum) :
        self.f.write('// function start\n')
        self.writeLabel(name)
        for _ in range(int(localNum)) :
            self.writePushPop(COMMANDTYPE['C_PUSH'], 'constant', 0)
        
    def writeCall(self, name, argNum) :
        global inputFileName
        returnAddress = inputFileName[:-3] + '$ret.' + str(self.returnAddressIndex)
        self.returnAddressIndex += 1
        self.f.write('// push returnAddress\n')
        self.writePushPop(COMMANDTYPE['C_PUSH'], 'constant', str(returnAddress));
        self.f.write('// push LCL, ARG, THIS, THAT\n')
        self.writePushPop(COMMANDTYPE['C_PUSH'], 'var', 'LCL');
        self.writePushPop(COMMANDTYPE['C_PUSH'], 'var', 'ARG');
        self.writePushPop(COMMANDTYPE['C_PUSH'], 'var', 'THIS');
        self.writePushPop(COMMANDTYPE['C_PUSH'], 'var', 'THAT');
        hackCode = f'// ARG = SP - 5 - nArgs\n'
        hackCode += f'@SP\n'
        hackCode += f'A=M\n'
        for _ in range(int(argNum) + 5) :
            hackCode += f'A=A-1\n'
        hackCode += f'D=A\n'
        hackCode += f'@ARG\n'
        hackCode += f'M=D\n'
        hackCode += f'// LCL = SP\n'
        hackCode += f'@SP\n'
        hackCode += f'D=M\n'
        hackCode += f'@LCL\n'
        hackCode += f'M=D\n'
        hackCode += f'// goto functionName\n'
        hackCode += f'@{name}\n'
        hackCode += f'0;JMP\n'
        hackCode += f'// (returnAddress)\n'
        hackCode += f'({returnAddress})\n'
        self.f.write(hackCode)

    def writeReturn(self) :
        hackCode = f'// endFrame=LCL\n'
        hackCode += f'@LCL\n'
        hackCode += f'D=M\n'
        hackCode += f'@endFrame\n'
        hackCode += f'M=D\n'
        hackCode += f'// retAddr = *(endFrame - 5)\n'
        hackCode += f'A=M-1\n'
        hackCode += f'A=A-1\n'
        hackCode += f'A=A-1\n'
        hackCode += f'A=A-1\n'
        hackCode += f'A=A-1\n'
        hackCode += f'D=M\n'
        hackCode += f'@retAddr\n'
        hackCode += f'M=D\n'
        hackCode += f'// *ARG = pop()\n'
        self.f.write(hackCode)
        self.writePushPop(COMMANDTYPE['C_POP'], 'argument', 0)
        hackCode = f'// SP = ARG + 1\n'
        hackCode += f'@ARG\n'
        hackCode += f'D=M\n'
        hackCode += f'@SP\n'  
        hackCode += f'M=D+1\n'
        inputTmpSegment = ['THAT', 'THIS', 'ARG', 'LCL']
        for i in range(len(inputTmpSegment)) :
            hackCode += f'// {inputTmpSegment[i]} = *(endFrame - {i + 1})\n'
            hackCode += f'@endFrame\n'
            hackCode += f'M=M-1\n'
            hackCode += f'A=M\n' 
            hackCode += f'D=M\n'
            hackCode += f'@{inputTmpSegment[i]}\n'
            hackCode += f'M=D\n'
        hackCode += f'// goto retAddr\n'
        hackCode += f'@retAddr\n'
        hackCode += f'A=M\n'
        hackCode += f'0;JMP\n'

        hackCode += f'// function end\n'
        self.f.write(hackCode)

def processFileName() :
    global outputFileName
    global targetDirectory

    argTool = argparse.ArgumentParser()
    argTool.add_argument('directoryName', type=str, help="Enter directory name")
    args = argTool.parse_args()
    args = args.directoryName
    fileList = os.listdir(args)
    for i in fileList :
        filename, fileExtension = os.path.splitext(args + '/' + i)
        if fileExtension == '.vm' :
            vmFileList.append(i)
    print(vmFileList)
    targetDirectory = args
    outputFileName = (vmFileList[0][:-3] \
        if len(vmFileList) == 1 and vmFileList[0] != 'Sys.vm' \
        else args) + '.asm'
    

# drives the process
def main() :
    global vmFileList
    global inputFileName
    global outputFileName

    processFileName()
    codeWriter = CodeWriter()
    for oneFile in vmFileList :
        inputFileName = oneFile
        parser = Parser()
        print(f'input: {inputFileName}, output: {outputFileName}')
        while True :
            if parser.parser(codeWriter) == -1:
                print(f'[File "{inputFileName}" Translate Complete]')
                break
            codeWriter.f.write(f'//// {parser.line} ////\n')

            if parser.type == COMMANDTYPE['C_ARITHMETIC'] :
                codeWriter.writeArithmetic(parser.arg1)
            elif parser.type == COMMANDTYPE['C_POP'] \
                or parser.type == COMMANDTYPE['C_PUSH'] :
                codeWriter.writePushPop(parser.type, parser.arg1, parser.arg2)
            elif parser.type == COMMANDTYPE['C_LABEL'] :
                codeWriter.writeLabel(parser.arg1)
            elif parser.type == COMMANDTYPE['C_GOTO'] :
                codeWriter.writeGoto(parser.arg1)
            elif parser.type == COMMANDTYPE['C_IF'] :
                codeWriter.writeIf(parser.arg1)
            elif parser.type == COMMANDTYPE['C_FUNCTION'] :
                codeWriter.writeFunction(parser.arg1, parser.arg2)
            elif parser.type == COMMANDTYPE['C_CALL'] :
                codeWriter.writeCall(parser.arg1, parser.arg2)
            elif parser.type == COMMANDTYPE['C_RETURN'] :
                codeWriter.writeReturn()
            
            print(f'종류: {parser.type}, 파라미터 {parser.arg1} {parser.arg2}')
            
    print(f'[All File Translate Complete : "{outputFileName}"]')

if __name__=="__main__":
    main()