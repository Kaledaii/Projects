                                             #    THE PERFECT GUESS

from playsound import playsound
import random
n=random.randint(1,100)
print("Welcome to 'The Perfect Guess'!")

guess=1
a=int(input("Enter your first guess (between 1 and 100): "))
while a!=n:
    if a<n:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess+=1    
    a=int(input("Enter your next guess: "))

print(f"Congratulations! You've guessed the perfect number {n} in {guess} attempts.")
playsound('bc.mp3')
