In this directory, I am trying to solve the n-queens problem.


implementation_1:
Use a 2-D array to mark the availability of positions on the board.
mark() - 4N 
next() - N*N


Implementation_2:
Use a set to mark the availability of positions on the board.
mark() - 4N
next() - N*N

Calculating 8-queen takes 2931.89 sec.

Implementation_3:
Use four 1D arrays to mark the availability of positions on the board.
mark() - constant
next() - N*N

The time complexity analysis seems to suggest that implementation 3 would have best performance.
In reality, however, implementation 2 runs the fastest.

This perhaps because next() in impl 2 is using a built-in iteration of a set object, thus 
is much faster than the next in impl 3.

Implementation_4
In this implementation, I used a totally different data structure:
An length N array where the value of each element represents the column col that has a queen.

Use only 38 secs to computer N=12.

Much better! This again the power of data structure. Use the right data structure and 
the performance enhancement can be great.