// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(MAINLOOP)
	@black
	M=0
	@KBD
	D=M
	@KBDFALSE
	D;JEQ
	@black
	M=-1
(KBDFALSE)
	@SCREENBLACK
	0;JMP


(SCREENBLACK)
	@SCREEN
	D=A
	@addr
	M=D
	
	@i
	M = 1
	
(SCREENLOOP)
	@i
	D = M
	@8192         // 전체 스크린 사이즈 8192개의 16비트
	D = D-A
	@MAINLOOP
	D;JGT
	
	@black
	D = M
	@addr
	A = M
	M = D
	@1
	D=A
	@addr
	M=D+M
	
	@i
	M = M+1
	@SCREENLOOP
	0;JMP
