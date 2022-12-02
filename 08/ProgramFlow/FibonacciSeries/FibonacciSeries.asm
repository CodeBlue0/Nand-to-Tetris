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
//// pop pointer 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put pointer 1
@1
D=A
@3
D=D+A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
//// push constant 0 ////
// get constant 0
@0
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop that 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put that 0
@0
D=A
@THAT
D=D+M
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
//// push constant 1 ////
// get constant 1
@1
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop that 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put that 1
@1
D=A
@THAT
D=D+M
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
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
//// push constant 2 ////
// get constant 2
@2
D=A
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
//// pop argument 0 ////
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
//// label MAIN_LOOP_START ////
// define label
(MAIN_LOOP_START)
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
//// if-goto COMPUTE_ELEMENT ////
// if-goto command
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@COMPUTE_ELEMENT
D;JGT
//// goto END_PROGRAM ////
// goto command
@END_PROGRAM
0;JMP
//// label COMPUTE_ELEMENT ////
// define label
(COMPUTE_ELEMENT)
//// push that 0 ////
// get that 0
@0
D=A
@THAT
A=D+M
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push that 1 ////
// get that 1
@1
D=A
@THAT
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
//// pop that 2 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put that 2
@2
D=A
@THAT
D=D+M
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
//// push pointer 1 ////
// get pointer 1
@1
D=A
@3
A=D+A
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push constant 1 ////
// get constant 1
@1
D=A
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
//// pop pointer 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put pointer 1
@1
D=A
@3
D=D+A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
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
//// push constant 1 ////
// get constant 1
@1
D=A
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
//// pop argument 0 ////
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
//// goto MAIN_LOOP_START ////
// goto command
@MAIN_LOOP_START
0;JMP
//// label END_PROGRAM ////
// define label
(END_PROGRAM)
