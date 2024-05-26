play = "yes"
QUESTION_FORMAT = "{}`\n A. {}\n B. {}\n C. {}\n D. {}\n Answer here: "

# Ask the user their name 
name = input("Whats your name? ")


# Greet and introduce the user to the quiz  
print("Welcome to my quiz {}".format(name))
print("This is a general knwoledge quiz.")

#check number of question attempts
while True:
    try:
        tries = input("How many attempts do you want? ")
        tries = int(tries)
        print("Cool, you will now get {} tries.".format(tries))
        break
    except:
        print("That is not a number.")

# Questions

while play == "yes":
    score = 0

    question_attempts1 = tries
    while question_attempts1 > 0:
        question1 = "How many planets are there in our solar system?"
        q1a = "5"
        q1b = "8"
        q1c = "7"
        q1d = "9"
        answer1 = input(QUESTION_FORMAT.format(question1, q1a, q1b, q1c, q1d))
        if answer1 == q1b or answer1 == "8":
            print("You are correct!")
            score += 1 
            break
        elif answer1 == "":
            print("You didn't type anything, but the answer was {}.".format(q1b))
        else:
            print("Incorrect. The anser was {}.".format(q1b))
        question_attempts1 -= 1
    
    