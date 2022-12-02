// Bootstrap
@256
D=A
@SP
M=D
@0
D=A
D=D-1
@LCL
M=D
D=D-1
@ARG
M=D
D=D-1
@THIS
M=D
D=D-1
@THAT
M=D
// push returnAddress
// get constant $ret.1
@$ret.1
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push LCL, ARG, THIS, THAT
// get var LCL
@LCL
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var ARG
@ARG
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THIS
@THIS
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THAT
@THAT
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@SP
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Sys.init
0;JMP
// (returnAddress)
($ret.1)
// // This file is part of www.nand2tetris.org
// // and the book "The Elements of Computing Systems"
// // by Nisan and Schocken, MIT Press.
// // File name: projects/08/FunctionCalls/StaticsTest/Class1.vm
// // Stores two supplied arguments in static[0] and static[1].
//// function Class1.set 0 ////
// function start
// define label
(Class1.set)
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
//// pop static 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 0
@Class1.0
D=A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
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
//// pop static 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 1
@Class1.1
D=A
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
//// return ////
// endFrame=LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame - 5)
A=M-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@retAddr
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
// THAT = *(endFrame - 1)
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function end
// // Returns static[0] - static[1].
//// function Class1.get 0 ////
// function start
// define label
(Class1.get)
//// push static 0 ////
// get static 0
@Class1.0
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push static 1 ////
// get static 1
@Class1.1
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
//// return ////
// endFrame=LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame - 5)
A=M-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@retAddr
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
// THAT = *(endFrame - 1)
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function end
// // This file is part of www.nand2tetris.org
// // and the book "The Elements of Computing Systems"
// // by Nisan and Schocken, MIT Press.
// // File name: projects/08/FunctionCalls/StaticsTest/Class2.vm
// // Stores two supplied arguments in static[0] and static[1].
//// function Class2.set 0 ////
// function start
// define label
(Class2.set)
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
//// pop static 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 0
@Class2.0
D=A
@popTmp2
M=D
@popTmp
D=M
@popTmp2
A=M
M=D
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
//// pop static 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put static 1
@Class2.1
D=A
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
//// return ////
// endFrame=LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame - 5)
A=M-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@retAddr
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
// THAT = *(endFrame - 1)
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function end
// // Returns static[0] - static[1].
//// function Class2.get 0 ////
// function start
// define label
(Class2.get)
//// push static 0 ////
// get static 0
@Class2.0
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push static 1 ////
// get static 1
@Class2.1
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
//// return ////
// endFrame=LCL
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame - 5)
A=M-1
A=A-1
A=A-1
A=A-1
A=A-1
D=M
@retAddr
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
// THAT = *(endFrame - 1)
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
// goto retAddr
@retAddr
A=M
0;JMP
// function end
// // This file is part of www.nand2tetris.org
// // and the book "The Elements of Computing Systems"
// // by Nisan and Schocken, MIT Press.
// // File name: projects/08/FunctionCalls/StaticsTest/Sys.vm
// // Tests that different functions, stored in two different 
// // class files, manipulate the static segment correctly. 
//// function Sys.init 0 ////
// function start
// define label
(Sys.init)
//// push constant 6 ////
// get constant 6
@6
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push constant 8 ////
// get constant 8
@8
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// call Class1.set 2 ////
// push returnAddress
// get constant Sys$ret.2
@Sys$ret.2
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push LCL, ARG, THIS, THAT
// get var LCL
@LCL
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var ARG
@ARG
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THIS
@THIS
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THAT
@THAT
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@SP
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class1.set
0;JMP
// (returnAddress)
(Sys$ret.2)
// // Dumps the return value
//// pop temp 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put temp 0
@0
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
//// push constant 23 ////
// get constant 23
@23
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push constant 15 ////
// get constant 15
@15
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// call Class2.set 2 ////
// push returnAddress
// get constant Sys$ret.3
@Sys$ret.3
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push LCL, ARG, THIS, THAT
// get var LCL
@LCL
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var ARG
@ARG
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THIS
@THIS
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THAT
@THAT
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@SP
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class2.set
0;JMP
// (returnAddress)
(Sys$ret.3)
// // Dumps the return value
//// pop temp 0 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put temp 0
@0
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
//// call Class1.get 0 ////
// push returnAddress
// get constant Sys$ret.4
@Sys$ret.4
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push LCL, ARG, THIS, THAT
// get var LCL
@LCL
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var ARG
@ARG
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THIS
@THIS
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THAT
@THAT
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@SP
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class1.get
0;JMP
// (returnAddress)
(Sys$ret.4)
//// call Class2.get 0 ////
// push returnAddress
// get constant Sys$ret.5
@Sys$ret.5
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// push LCL, ARG, THIS, THAT
// get var LCL
@LCL
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var ARG
@ARG
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THIS
@THIS
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// get var THAT
@THAT
D=M
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP - 5 - nArgs
@SP
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Class2.get
0;JMP
// (returnAddress)
(Sys$ret.5)
//// label WHILE ////
// define label
(WHILE)
//// goto WHILE ////
// goto command
@WHILE
0;JMP
