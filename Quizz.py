import random

print()
print("Math Quiz")
print()

# yes/no functions


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return instruction()
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instruction():
    print(''' 
               ***INSTRUCTIONS***

In this quiz I will be testing you with basic math questions
that will vary from addition, subtraction, multiplication and division.
There will be multiple levels and the difficulty will slowly get harder.
There isn't that much to say so... Are you ready?
         
         ''')


yes_no("do you wish to see instructions?")

# start the game
print("Press [enter] to start")
input()

print("***Level 1***")

num_1 = random.randint(1, 5)
num_2 = random.randint(1, 5)


def math_equation():
    math_result = random.randint(1, 6)
    return math_result


def operation():


def multiplication(num_1, num_2):
    return num_1 * num_2


def addition(num_1, num_2):
    return num_1 + num_2



def subtraction(num_1, num_2):
    return num_1 - num_2



operation = [multiplication, addition, subtraction]


if operation == multiplication():
    question = f"{num_1} * {num_2} ="
elif operation == addition:
    question = f"{num_1} + {num_2} ="
elif operation == subtraction:
    question = f"{num_1} - {num_2} ="


    elif selected_operation == subtraction:
        question = f"{num_1} - {num_2} ="
        answer = subtraction(num_1, -num_2)

