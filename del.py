

import random
a=random.randint(1,100)
i=5

while i>0:
    x=int(input())
    if x==a:
        print("you wom")
        break
    elif x>a:
        print("gussed number is larger than a")
        i-=1
    else:
        print("guessed number is smaller than a")
        i-=1
else:
    print("you lost")
    print(a)
        
        
