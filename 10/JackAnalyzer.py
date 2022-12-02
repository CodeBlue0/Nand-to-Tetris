import argparse
from asyncore import write
from glob import glob
import os
from msilib.schema import Directory
from symtable import SymbolTable
from textwrap import fill

jackFileList = []
outputFileTList = []
outputFileList = []

def processFileName() :
    global outputFileName
    global outputFileList
    global outputFileTList

    argTool = argparse.ArgumentParser()
    argTool.add_argument('directoryName', type=str, help="Enter directory name")
    args = argTool.parse_args()
    args = args.directoryName
    fileList = os.listdir(args)
    for i in fileList :
        filename, fileExtension = os.path.splitext(args + '/' + i)
        if fileExtension == '.jack' :
            jackFileList.append(filename)
            outputFileList.append(filename + '.xml')
            outputFileTList.append(filename + 'T.xml')

    print(f'jackFileList : {jackFileList}')
    print(f'outputFileList : {outputFileList}')
    print(f'outputFileTList : {outputFileTList}')
    

# drives the process
def main() :
    processFileName()
    


if __name__=="__main__":
    main()