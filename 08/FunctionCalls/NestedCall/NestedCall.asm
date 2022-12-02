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
// // Sys.vm for NestedCall test.
// // Sys.init()
// //
// // Calls Sys.main() and stores return value in temp 1.
// // Does not return.  (Enters infinite loop.)
//// function Sys.init 0 ////
// function start
// define label
(Sys.init)
// // test THIS and THAT context save
//// push constant 4000 ////
// get constant 4000
@4000
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop pointer 0 ////
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
//// push constant 5000 ////
// get constant 5000
@5000
D=A
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
//// call Sys.main 0 ////
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
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Sys.main
0;JMP
// (returnAddress)
(Sys$ret.2)
//// pop temp 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put temp 1
@1
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
//// label LOOP ////
// define label
(LOOP)
//// goto LOOP ////
// goto command
@LOOP
0;JMP
// // Sys.main()
// //
// // Sets locals 1, 2 and 3, leaving locals 0 and 4 unchanged to test
// // default local initialization to 0.  (RAM set to -1 by test setup.)
// // Calls Sys.add12(123) and stores return value (135) in temp 0.
// // Returns local 0 + local 1 + local 2 + local 3 + local 4 (456) to confirm
// // that locals were not mangled by function call.
//// function Sys.main 5 ////
// function start
// define label
(Sys.main)
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
// get constant 0
@0
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// push constant 4001 ////
// get constant 4001
@4001
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop pointer 0 ////
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
//// push constant 5001 ////
// get constant 5001
@5001
D=A
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
//// push constant 200 ////
// get constant 200
@200
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop local 1 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put local 1
@1
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
//// push constant 40 ////
// get constant 40
@40
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop local 2 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put local 2
@2
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
//// pop local 3 ////
// pop from stack
@SP
M=M-1
@SP
A=M
D=M
@popTmp
M=D
// put local 3
@3
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
//// push constant 123 ////
// get constant 123
@123
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// call Sys.add12 1 ////
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
D=A
@ARG
M=D
// LCL = SP
@SP
D=M
@LCL
M=D
// goto functionName
@Sys.add12
0;JMP
// (returnAddress)
(Sys$ret.3)
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
//// push local 2 ////
// get local 2
@2
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
//// push local 3 ////
// get local 3
@3
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
//// push local 4 ////
// get local 4
@4
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
//// add ////
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
//// add ////
// add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
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
// // Sys.add12(int n)
// //
// // Returns n+12.
//// function Sys.add12 0 ////
// function start
// define label
(Sys.add12)
//// push constant 4002 ////
// get constant 4002
@4002
D=A
// push to stack
@SP
A=M
M=D
@SP
M=M+1
//// pop pointer 0 ////
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
//// push constant 5002 ////
// get constant 5002
@5002
D=A
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
//// push constant 12 ////
// get constant 12
@12
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
