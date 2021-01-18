import random
import sys

number=random.randint(0,9)
def guess():
    g=int(input("Guess the Number = "))
    
    if g<number:
        print("The Number should be Gerater then you have to enter")
        guess()
    elif g>number:
        print("The Number should be Lesser then you have to enter")
        guess()
    else:
        print("Write Guess the Number is",number)
        sys.exit()
guess()
