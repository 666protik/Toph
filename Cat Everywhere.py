'''
Cats everywhere! I came back home after being far away for a long time.
Kitty, Puffy, Neffy, Toffy, Kiffy, Soffy, Kulffy, Wol
Two of my sisters are very fond of cats. So many cats stay at our home.
 My sisters give them a different name (Kitty, Puffy, Neffy, Toffy, Kiffy, 
 Soffy, Kulffy, Wolffy, Borffy). Here Kitty is the oldest cat, then Puffy 
 and so on. Borffy is the youngest cat. Every time my sisters tell me about 
 their name and age, I instantly forget them.
It's too confusing to me. So I came up with a plan that I will name them by 
number (1, 2, 3...). But seeing those cats names I find out one thing.
 My sisters love "ffy" at the end of a cat's name. So I will name them like this 
 (Iffy, 2ffy, 3ffy, 4ffy, ...) oldest to youngest.
Now if anyone asks me, "Who is the 3rd oldest cat?". I can instantly say "3ffy".
 Did you get my idea?
In this problem, I will give you the name of nth oldest cat. You have to say me 
the name of (n + 1) ^ (th) oldest cat (so that I can be sure that you understood 
my idea of cat's naming)

            Input               Output
             5ffy                6ffy
'''

N=input().strip()
ans=int(N[:-3])+1
print(f'{ans}ffy')
