'''
Given an integer N, print the N-th Fibonacci number.

A Fibonacci series is a series of numbers in which each number
 is the sum of the two numbers preceding it. For this problem,
 you can assume that the first two numbers in the series are 1 and 1.
 Below you can see the first few numbers of the series:
 1, 1, 2, 3, 5, 8, ...
 
Input: 3
Output: 2
'''
N = int(input())
a,b=0,1
for _ in range (N):
	a,b=b,a+b
print(a)
