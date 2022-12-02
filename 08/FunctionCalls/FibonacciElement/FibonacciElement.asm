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
// // File name: projects/08/FunctionCalls/FibonacciElement/Main.vm
// // Computes the n'th element of the Fibonacci series, recursively.
// // n is given in argument[0].  Called by the Sys.init function 
// // (part of the Sys.vm file), which also pushes the argument[0] 
// // parameter before this code starts running.
//// function Main.fibonacci 0 ////
// function start
// define label
(Main.fibonacci)
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
// // checks if n<2
//// lt ////
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@SETTRUE0
D;JLT
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
//// if-goto IF_TRUE ////
// if-goto command
// pop from stack
@SP
M=M-1
A=M
D=M
@IF_TRUE
D;JNE
//// goto IF_FALSE ////
// goto command
@IF_FALSE
0;JMP
// // if n<2, return n
//// label IF_TRUE ////
// define label
(IF_TRUE)
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
// // if n>=2, returns fib(n-2)+fib(n-1)
//// label IF_FALSE ////
// define label
(IF_FALSE)
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
// // computes fib(n-2)
//// call Main.fibonacci 1 ////
// push returnAddress
// get constant Main$ret.2
@Main$ret.2
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
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Main.fibonacci
0;JMP
// (returnAddress)
(Main$ret.2)
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
// // computes fib(n-1)
//// call Main.fibonacci 1 ////
// push returnAddress
// get constant Main$ret.3
@Main$ret.3
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
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Main.fibonacci
0;JMP
// (returnAddress)
(Main$ret.3)
// // returns fib(n-1) + fib(n-2)
//// add ////
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
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
// // File name: projects/08/FunctionCalls/FibonacciElement/Sys.vm
// // Pushes a constant, say n, onto the stack, and calls the Main.fibonacii
// // function, which computes the n'th element of the Fibonacci series.
// // Note that by convention, the Sys.init function is called "automatically" 
// // by the bootstrap code.
//// function Sys.init 0 ////
// function start
// define label
(Sys.init)
//// push constant 4 ////
// get constant 4
@4
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
// // computes the 4'th fibonacci element
//// call Main.fibonacci 1 ////
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
@Main.fibonacci
0;JMP
// (returnAddress)
(Sys$ret.4)
//// label WHILE ////
// define label
(WHILE)
// // loops infinitely
//// goto WHILE ////
// goto command
@WHILE
0;JMP
