// push constant 17
@17
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE0
D;JEQ
@SP
A=M-1
A=A-1
M=0
@END0
0;JMP
(SETTRUE0)
@SP
A=M-1
A=A-1
M=-1
@END0
0;JMP
(END0)
@SP
M=M-1
// push constant 17
@17
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE1
D;JEQ
@SP
A=M-1
A=A-1
M=0
@END1
0;JMP
(SETTRUE1)
@SP
A=M-1
A=A-1
M=-1
@END1
0;JMP
(END1)
@SP
M=M-1
// push constant 16
@16
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE2
D;JEQ
@SP
A=M-1
A=A-1
M=0
@END2
0;JMP
(SETTRUE2)
@SP
A=M-1
A=A-1
M=-1
@END2
0;JMP
(END2)
@SP
M=M-1
// push constant 892
@892
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE3
D;JLT
@SP
A=M-1
A=A-1
M=0
@END3
0;JMP
(SETTRUE3)
@SP
A=M-1
A=A-1
M=-1
@END3
0;JMP
(END3)
@SP
M=M-1
// push constant 891
@891
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE4
D;JLT
@SP
A=M-1
A=A-1
M=0
@END4
0;JMP
(SETTRUE4)
@SP
A=M-1
A=A-1
M=-1
@END4
0;JMP
(END4)
@SP
M=M-1
// push constant 891
@891
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE5
D;JLT
@SP
A=M-1
A=A-1
M=0
@END5
0;JMP
(SETTRUE5)
@SP
A=M-1
A=A-1
M=-1
@END5
0;JMP
(END5)
@SP
M=M-1
// push constant 32767
@32767
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE6
D;JGT
@SP
A=M-1
A=A-1
M=0
@END6
0;JMP
(SETTRUE6)
@SP
A=M-1
A=A-1
M=-1
@END6
0;JMP
(END6)
@SP
M=M-1
// push constant 32766
@32766
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE7
D;JGT
@SP
A=M-1
A=A-1
M=0
@END7
0;JMP
(SETTRUE7)
@SP
A=M-1
A=A-1
M=-1
@END7
0;JMP
(END7)
@SP
M=M-1
// push constant 32766
@32766
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE8
D;JGT
@SP
A=M-1
A=A-1
M=0
@END8
0;JMP
(SETTRUE8)
@SP
A=M-1
A=A-1
M=-1
@END8
0;JMP
(END8)
@SP
M=M-1
// push constant 57
@57
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
D=A
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
// push constant 112
@112
D=A
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
// neg
@SP
A=M-1
M=-M
// and
@SP
A=M-1
D=M
A=A-1
M=D&M
@SP
M=M-1
// push constant 82
@82
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
A=M-1
D=M
A=A-1
M=D|M
@SP
M=M-1
// not
@SP
A=M-1
M=!M
