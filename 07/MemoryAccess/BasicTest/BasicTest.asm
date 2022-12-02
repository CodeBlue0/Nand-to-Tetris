// push constant 10
// get constant 10
@10
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop local 0
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
// push constant 21
// get constant 21
@21
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 22
// get constant 22
@22
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop argument 2
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put argument 2
@2
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
// pop argument 1
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put argument 1
@1
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
// push constant 36
// get constant 36
@36
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop this 6
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put this 6
@6
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
// push constant 42
// get constant 42
@42
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 45
// get constant 45
@45
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop that 5
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put that 5
@5
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
// pop that 2
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
// push constant 510
// get constant 510
@510
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// pop temp 6
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put temp 6
@6
D=A
@5
D=D+A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
// push local 0
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
// push that 5
// get that 5
@5
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
// push argument 1
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
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
// push this 6
// get this 6
@6
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
// push this 6
// get this 6
@6
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
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
// push temp 6
// get temp 6
@6
D=A
@5
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
