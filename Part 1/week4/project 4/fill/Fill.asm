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

    @8192
    D=A
    @n
    M=D     // n = 8192
    @SCREEN
    D=A
    @n
    M=D+M   // n = SCREEN[n] = SCREEN[8192]

(LOOP)
    @SCREEN
    D=A
    @address
    M=D     // address = SCREEN[0]

    // if KBD != 0 blacken SCREEN, else whiten
    @KBD
    D=M
    @i
    M=0     // i = 0
    @SCREEN_LOOP
    D;JEQ   // if KBD == 0 then goto SCREEN_LOOP
    @i
    M=-1    // if KBD != 0 then i = -1

(SCREEN_LOOP)
    @n
    D=M
    @address
    D=D-M;
    @END
    D;JEQ   // if address == n goto END

    @i
    D=M
    @address
    A=M
    M=D    // set to i

    @address
    M=M+1   // address = address + 1

    @SCREEN_LOOP
    0;JMP   // goto SCREEN_LOOP

(END)
    @LOOP
    0;JMP   // goto LOOP
