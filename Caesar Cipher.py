'''
Byang wants to write a secret message to his friend.
He has recently discovered Caesar Cipher.
Caesar cipher is simple encryption techniques where each letter in the
 message is replaced by a letter some fixed number of positions down the alphabet.
For example, with a left shift of 2, C would be replaced by A, D would become B, and so on.

Letters:
ABCDEFGHIJKLMNOPQRSTUVWXYZ

After applying Caesar cipher of left shift 2:
YZABCDEFGHIJKLMNOPQRSTUVWX

        Input                       Output
          2                       fcjjm umpjb
      hello world
'''
n = int(input().strip())
text = input()

result = ""

for ch in text:             # ch = character
    if ch == " ":
        result = result + " "
    else:
        pos = ord(ch) - ord('a')        #ord() function ch gives ASCII value
        new_pos = (pos - n) % 26        #alphabet has 26 letter
        new_char = chr(new_pos + ord('a'))      #chr() change number to letter
        result = result + new_char
print(result)
