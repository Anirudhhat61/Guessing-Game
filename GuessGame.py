import random
#variables defined
n = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99 here :"))
#loop
while n != "guess":
    print
    if guess < n:
        print ("Guess is low ")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("Guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("Guessed it !!")
        break
    print