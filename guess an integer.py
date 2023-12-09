import random
num=random.randint(1,100)
while (1):
    guess=int(input("Guess number between 1 and 100: "))
    if guess==num:
        print("Your guess is correct ")
        break
    elif guess < num:
        print("Guess higher integer ")
    else:
        print("Guess lower integer ")
        
