import random

print()
print("➕➖Math Quiz✖️➗")
print()

# this is to show what multiplication question looks like.


def multiplication(num_1, num_2):
    return num_1 * num_2


# this is to show what addition question looks like.
def addition(num_1, num_2):
    return num_1 + num_2


# this shows the math operations
def operation():
    return random.choice([multiplication, addition, ])


def math_equation():
    return random.randint(1, 15)


# function for yes no questions
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return instruction()
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


# Instructions
def instruction():
    print(''' 
               ***INSTRUCTIONS***

In this quiz, I will be testing you with basic math questions
that will vary from addition, subtraction, multiplication, and division.
There will be multiple levels, and the difficulty will slowly get harder.
There isn't that much to say so... Are you ready?

         ''')


yes_no("Do you wish to see instructions? ")
print()


# Asking for the number of rounds (chat gpt 38 - 40)
num_questions = input("How many questions do you want to answer? ")
while not num_questions.isdigit():
    # this is if you entered anything other than a number
    print("please enter a number.")
    # this is asking how many questions you want to answer
    num_questions = input("how many questions do you want to answer? ")
num_questions = int(num_questions)
for Question_number in range(1, num_questions + 1):
    print()
    print(f"*** Question {Question_number} ***")
    # this is showing what numbers the question can use up to.
    num_1 = random.randint(1, 15)
    num_2 = random.randint(1, 15)
    # this is to show what operation is being used
    selected_operation = operation()

    # this is to show the equation
    if selected_operation == multiplication:
        question = f"{num_1} * {num_2} ="
        print()
        answer = multiplication(num_1, num_2)
    elif selected_operation == addition:
        question = f"{num_1} + {num_2} ="
        print()
        answer = addition(num_1, num_2)


    # this is chat gpt (87 - 91)
    print(question)
    # this lets us enter your own answer
    user_answer = input("Your answer: ")
    while not user_answer.isdigit():

        # this is if you have entered something other than a number
        print("Please enter a number.")
        user_answer = input("Your answer: ")
    user_answer = int(user_answer)

    # this shows if you right or not (my code)
    if user_answer == answer:
        print("You got it right!")
    else:
        # this shows you the real answer if you got it wrong
        print(f"Wrong! The right answer is {answer}.")


