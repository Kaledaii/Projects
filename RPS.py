# Rock Paper Scissior game
''' rock=1  paper=2  scissior=3'''

import time
from playsound import playsound
import random
computer=random.choice([1,2,3])

chstr=input("Enter your move r/p/s ").lower()
dic={'r':1,'p':2,'s':3}
ch=dic[chstr]
revdic={1:'Rock🪨',2:'Paper📄',3:'Scissior✂️'}
print(f"You chose {revdic[ch]}  and Computer chose {revdic[computer]}")
print(f'Its {revdic[ch]}  v/s  {revdic[computer]}\n')

for i in range(3,0,-1):
    print(f"Showdown:{i}\r",end="")
    time.sleep(1)
print()

if(ch==computer):
    print('🤝It\'s a draw')
    playsound('draw.wav')

else:
    if(computer==1 and ch==3):
        print('You lose !😢')
        playsound('cry.mp3')

    if(computer==1 and ch==2):
        print('You win !🎉')
        playsound('clap.wav')

    if(computer==2 and ch==1):
        print('You lose !😢')
        playsound('cry.mp3')

    if(computer==2 and ch==3):
        print('You win !🎉')
        playsound('clap.wav')

    if(computer==3 and ch==1):
        print('You win !🎉')
        playsound('clap.wav')

    if(computer==3 and ch==2):
        print('You lose !😢')
        playsound('cry.mp3')

    