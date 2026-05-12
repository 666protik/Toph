'''
Byang is learning how to add numbers. However, he gets confused whenever there is a carry.
To help Byang you need to write a program that will read two integers and determine
if Byang will encounter any carry when adding these two numbers.

For example when adding 182 and 243 Byang will encounter a carry:
  182
+ 243
-----
    5 (Carry 0)
  ---
   25 (Carry 1; This will confuse Byang)
  ---
  425 (Carry 0)

On the other hand, when adding 123 and 321 Byang will not encounter any carry,
and it will not confuse Byang:
  123
+ 321
-----
    4 (Carry 0)
  ---
   44 (Carry 0)
  ---
  444 (Carry 0)

     Input                   Output
    182 243                   Yes
    123 321                    No
'''

a, b = map(int, input().split())

while a or b:
    if a%10 + b%10 >= 10:
        print("Yes")
        exit()
    a=a//10
    b=b//10

print("No")
