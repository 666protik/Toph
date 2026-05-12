'''
Given an integer N, print a full pyramid of asterisks.
A full pyramid of asterisks of size N has N lines of asterisks.

Here is a full pyramid of asterisks of size 4:
   *
  * *
 * * *
* * * *

    Input           Output
      3               *
                     * *
                    * * *
'''
n = int(input().strip())

for i in range (1, n+1):
    space = (n-i) * " "
    star = "*" + " *" * (i-1)
    print(space+star)
