'''
Geralt of Rivia is a legendary witcher of the School of the Wolf active 
throughout the 13th century. During the Trial of the Grasses or Herbs,
Geralt exhibited unusual tolerance for the mutagens that grant witchers 
their abilities. Accordingly, Geralt was subjected to further experimental
mutagens which rendered his hair white and may have given him greater speed,
strength, and stamina than his fellow witchers. After undergoing the trial,
Geralt became a powerful monster slayer.

Geralt's story is not one of those heroes, instead it's a story of a professional.
His profession is to kill monsters. But he only kills a monster if its evil or
harmful to other beings. How does he determine if the monster is harmful you may ask.
Well, it's in the name of the monsters. If the name of the monster contains any
single vowel (a, e, i, o, u), the monster is considered as evil.

In this problem, you will be given the names of the monsters. You have to determine
whether Geralt will kill them or not.

    Input                Output
      2                    No
     ynfr                  Yes
     odimm
'''

t = int(input().strip())

Vowel = {'a', 'e', 'i', 'o', 'u'}

for _ in range(t):
    s = input().strip().lower()

    for ch in s:
        if ch in Vowel:
            print("Yes")
            break
    else:
            print("No")
