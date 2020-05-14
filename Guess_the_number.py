import random
print("Hello, what is your name?")
name = input()
print("Well, " + name + " I am thinking of a number between 1 and 7")
number = random.randint(1, 7)

for count in range(1, 6):
    guess = int(input("Take a guess!"))
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Good job!")
        break
if guess == number:
    print("You took " + str(count) + " guesses!")

else:
    print("Nope, the number I was thinking of is " + str(number))