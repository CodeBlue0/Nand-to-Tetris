// push constant 111
// get constant 111
@111
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 333
// get constant 333
@333
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 888
// get constant 888
@888
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop static 8
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 8
@StaticTest.8
D=A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
// pop static 3
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 3
@StaticTest.3
D=A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
// pop static 1
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 1
@StaticTest.1
D=A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
// push static 3
// get static 3
@StaticTest.3
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push static 1
// get static 1
@StaticTest.1
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
// push static 8
// get static 8
@StaticTest.8
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
