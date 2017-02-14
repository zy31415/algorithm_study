In this directory, I am trying to solve the n-queens problem.


implementation_1:
Use a 2-D array to mark the availability of positions on the board.
mark() - 4N 
next() - N*N


Implementation_2:
Use a set to mark the availability of positions on the board.
mark() - 4N
next() - N*N

Implementation_3:
Use four 1D arrays to mark the availability of positions on the board.
mark() - constant
next() - N*N

The time complexity analysis seems to suggest that implementation 3 would have best performance.
In reality, however, implementation 2 runs the fastest.

This perhaps because next() in impl 2 is using a built-in iteration of a set object, thus 
is much faster than the next in impl 3.

