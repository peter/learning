# Nand to Tetris Coursera Course

## Project 1

"A typical computer architecture is based on a set of elementary logic gates like And, Or, Mux, etc., as well as their bit-wise versions And16, Or16, Mux16, etc. (assuming a 16-bit machine). This project engages you in the construction of a typical set of basic logic gates. These gates form the elementary building blocks from which more complex chips will be later constructed."

"Build all the logic gates described in Chapter 1 (see list below), yielding a basic chip-set. The only building blocks that you can use in this project are primitive Nand gates and the composite gates that you will gradually build on top of them."

* Not
* And
* Or
* Xor
* Mux
* DMux
* Not16
* And16
* Or16
* Mux16
* Or8Way
* Mux4Way16
* Mux8Way16
* DMux4Way
* DMux8Way

## Project 2

Arithmetic Logic Unit

"in 1945 the mathematician John Von Neumann wrote a seminal paper in which he included a diagram or a description of how general purpose computers can be built. And this became to be known over the years as the Von Neumann Architecture. Now, when you look at this diagram, you see that one key player in the diagram is the central processing unit and within this CPU, yet another important piece the ALU or the Arithmetic Logic Unit"

Some of these functions are arithmetic and some of these functions are logical. So for example common computations that ALU typically perform are integer addition, integer multiplication, integer division.

"if for some reason you decide that the ALU will not include multiplication or division, presumably at a later point when you build your software layer you will deal, you will complete this functionality with software."

the Hack ALU

the ALU has two 16-bit data inputs which we call x and y. It outputs a single 16-bit output which we call out, which function to compute is determined by six control bits that have strange names like zx and nx and so on

18 functions only

 when you set out to build the chips of Project 2, you can certainly use all the chips that you built In Project 1

The HalfAdder takes two bits, and adds them up, and outputs both the sum of these two bits and the carry bit, which may be either 0 or 1

FullAdder is slightly more powerful than the HalfAdder. It is capable of summing up three incoming bits, so to speak and it outputs the same thing, the sum of the three bits and the carry.

you can build a FullAdder using two HalfAdders.

## Resources

* [Coursera Course Homepage](https://www.coursera.org/learn/build-a-computer/home/welcome)
* [Nand2Tetris Homepage](https://www.nand2tetris.org/)

* [HDL Survival Guide](https://www.ic.unicamp.br/~rodolfo/Cursos/mc404/2020s1/HDL_Survival_Guida-Nand2tetris.pdf)

Project 1:

* [Problem Description](https://www.nand2tetris.org/project01)
* [Lecture Notes: Boolean Logic](https://drive.google.com/file/d/1MY1buFHo_Wx5DPrKhCNSA2cm5ltwFJzM/view)
* [PDF: Boolean Logic](https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/44046b_f2c9e41f0b204a34ab78be0ae4953128.pdf)
* [HDL Guide](https://drive.google.com/file/d/1dPj4XNby9iuAs-47U9k3xtYy9hJ-ET0T/view)
* [Hardware Simulator Tutorial](https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/44046b_02055f8bb5ac47648c0ab642f01c1919.pdf)

Project 2:

* [PDF: Boolean Arithmetic](https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/44046b_89c60703ebfc4bf39acef13bdc050f5d.pdf)
* [HDL Guide](https://drive.google.com/file/d/1dPj4XNby9iuAs-47U9k3xtYy9hJ-ET0T/view)
* [The Hack Chipset](https://drive.google.com/file/d/1IsDnH0t7q_Im491LQ7_5_ajV0CokRbwR/view)