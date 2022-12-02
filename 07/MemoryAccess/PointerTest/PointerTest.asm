// push constant 3030
// get constant 3030
@3030
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put pointer 0
@0
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
// push constant 3040
// get constant 3040
@3040
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
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
// push constant 32
// get constant 32
@32
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop this 2
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put this 2
@2
D=A
@THIS
D=D+M
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
// push constant 46
// get constant 46
@46
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop that 6
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put that 6
@6
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
// push pointer 0
// get pointer 0
@0
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
// push pointer 1
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
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
// push this 2
// get this 2
@2
D=A
@THIS
A=D+M
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
// push that 6
// get that 6
@6
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
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
