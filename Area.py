'''In this problem, you will be given a square which has a length of n.
   Co-ordinates of the square are (0,0), (n,0), (n,n), (0,n).

You need to draw 4 straight lines:
    1.Line from (0,1) to (n,n−1)
    2.Line from (1,0) to (n−1,n)
    3.Line from (0,n−1) to (n,1)
    4.Line from (1,n) to (n−1,0)

These four lines will intersect at a point (x,y) like the figure shown below.
Calculate the total area of A+B+C+D (except the four corner unit square).

    Input                   Output
      1                    Case 1:8
      6
'''

t = int(input().strip())

for case in range(1, t + 1):
    
    n = int(input().strip())
    ans = 2 * n - 4
    print(f"Case {case}: {ans}")
