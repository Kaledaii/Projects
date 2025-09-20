# Rock Paper Scissior game
''' rock=1  paper=2  scissior=3'''

import random
computer=random.choice([1,2,3])

chstr=input("Enter your move r/p/s ").lower()
dic={'r':1,'p':2,'s':3}
ch=dic[chstr]
revdic={1:'Rock',2:'Paper',3:'Scissior'}
print(f"You chose {revdic[ch]} and Computer chose {revdic[computer]}")

if(ch==computer):
    print('It\'s a draw')
else:
    if(computer==1 and ch==3):
        print('You lose !')
    if(computer==1 and ch==2):
        print('You win !')
    if(computer==2 and ch==1):
        print('You lose !')
    if(computer==2 and ch==3):
        print('You win !')
    if(computer==3 and ch==1):
        print('You win !')
    if(computer==3 and ch==2):
        print('You lose !')
    