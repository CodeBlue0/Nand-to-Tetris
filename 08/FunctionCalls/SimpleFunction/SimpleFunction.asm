// // This file is part of www.nand2tetris.org
// // and the book "The Elements of Computing Systems"
// // by Nisan and Schocken, MIT Press.
// // File name: projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm
// // Performs a simple calculation and returns the result.
//// function SimpleFunction.test 2 ////
// function start
// define label
(SimpleFunction.test)
// get constant 0
@0
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get constant 0
@0
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push local 0 ////
// get local 0
@0
D=A
@LCL
A=D+M
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push local 1 ////
// get local 1
@1
D=A
@LCL
A=D+M
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// add ////
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
//// not ////
// not
@SP
A=M-1
M=!M
//// push argument 0 ////
// get argument 0
@0
D=A
@ARG
A=D+M
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// add ////
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
//// push argument 1 ////
// get argument 1
@1
D=A
@ARG
A=D+M
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// sub ////
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
// // return
//// return ////
// endFrame=LCL
@LCL
D=M
@endFrame
M=D
// *ARG = pop()
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put argument 0
@0
D=A
@ARG
D=D+M
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(endFrame - 0)
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
// THIS = *(endFrame - 1)
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
// ARG = *(endFrame - 2)
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
// LCL = *(endFrame - 3)
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
// goto *(endFrame - 5)
@endFrame
M=M-1
A=M
A=M
0;JMP
// function end
