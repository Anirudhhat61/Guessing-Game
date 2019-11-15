import random

min = 1
max = 6

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print ("Started Rolling the dices ")
    print("Values Is ")
    print(random.randint (min,max))
    print(random.randint(min, max))

    roll_again = input("Roll the dices again (yes/y) : ")
else:
    print("Thanks for playing")