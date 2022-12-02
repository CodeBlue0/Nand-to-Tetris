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
//// pop local 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put local 0
@0
D=A
@LCL
D=D+M
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
//// label LOOP_START ////
// define label
(LOOP_START)
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
//// add ////
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
//// pop local 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put local 0
@0
D=A
@LCL
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
//// if-goto LOOP_START ////
// if-goto command
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@LOOP_START
D;JGT//// push local 0 ////
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
