import random
num1 = random.randint(0, 100)
hello = int(input('Guess a number between 1 and a 100: '))
while hello != num1:

    if hello > num1:
        print("Too High")
        hello = int(input("Enter the Number again: "))
    elif hello < num1:
        print("Too Low")
        hello = int(input("Enter the number again"))
    else:
        break

exit("Yaay!! You Got It!!")










