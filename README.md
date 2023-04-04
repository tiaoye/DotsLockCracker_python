### DotLockCracker_py

#### Introduction

This is a python version of the project [Atomic Heart Dots Lock Cracker](https://github.com/H-Shen/DotsLockCracker) that helps players unlock dots lock quickly in the game **Atomic Heart**.
The user needs to input two arrays that represent the original pattern and the target pattern of the lock,
and the app will output one possible sequence of the shortest path to unlock the lock by
pressing the corresponding sequence of keys on the PS5 controller.

#### Installation

Download the python script and make sure python is installed in your system.

#### Usage

After running the app, it will ask for the original pattern and the target pattern. The pattern is a line of a string consisting
of eight character separated by a single space, such as **0 0 0 0 0 0 0 0**. Here, we use each number to represent status in one
dot in the circle lock.

The default mapping of numbers to colors is 0 for no-color, 1 for yellow, 2 for blue, 3 for red, etc.
The user can define a unique number for each color as long as the mapping rule has no conflicts and
is the same for both patterns. Note that the app only allows numbers between 0 and 8.

Additionally, the pattern starts from 12 o'clock and goes clockwise, where the first number in the array represents
the status of the slot in the 12 o'clock direction.

For example, the original pattern of the lock below is **3 0 0 0 0 0 1 3**, and the target pattern is on the outer round of the lock,
which is **0 3 1 0 0 0 3 0** here:


```shell
# Usage: python dotsLockCracker.py --o <original pattern> --p <pattern to crack>
python dotsLockCracker.py --o 30000013 --p 03100030
```

![png](./1.png)

After inputting the two patterns, the app will print out the number of steps required on the shortest path,
the updated status of the lock on each step, and the sequence of controller keys for PS5 required to unlock the lock:

```shell
Minimum number of steps:11
30000013  ->  00001330  :  L2
00001330  ->  00013030  :  X
00013030  ->  00030130  :  X
00030130  ->  30000301  :  R2
30000301  ->  30003001  :  X
30003001  ->  00300130  :  L2
00300130  ->  00301030  :  X
00301030  ->  00310030  :  X
00310030  ->  30003100  :  R2
30003100  ->  30031000  :  X
30031000  ->  03100030  :  L2
```

Just follow the sequence to unlock.

#### note
- the string can contain whether digit or any other characters, for instance **3 0 0 0 0 0 1 3** and **r n n n n n y r** are both valid input.