'''
Given an integer N, print the trailing 4 digits of N! (N factorial).

    N	    Factorial (N!N!)	    Last 4 Digits
    3	    6	                           6
    7	    5040	                    5040
    11  	39916800	                6800
    15	    1307674368000           	8000

    Input           Output
      4               24  
      10             8800

'''

import math

f = math.factorial(int(input().strip()))

if f >= 1000:
    print(f"{f % 10000:04d}")
else:
    print(f)
