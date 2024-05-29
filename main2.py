play = "yes"
QUESTION_FORMAT = "{}`\n A. {}\n B. {}\n C. {}\n D. {}\n Answer here: "
GOOD_COMMENTS=["well done","great work",]
BAD_COMMENTS=["your not very smart","bad job"]

QUESTIONS = ["How many planets are there in our solar system?",
                "How many types of ducks are there?",
                    "How many sheeps are in New Zealand?"]

OPTIONS = [["5", "8", "7", "9"], 
            ["162", "257","64","4"], 
                ["65 million", "10 million", "8 million", "20 million"]]
SHORT_OPTIONS = ["a, b, c, d"]
ANSWERS = [1, 0, 3]

import random
# Ask the user their name 
name = input("What is your name? ")

# Greet and introduce the user to the quiz  
print("Welcome to my quiz {}".format(name))
print("This is a general knowledge quiz.")

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

    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                    OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("Correct!")
                score += 5
                print(random.choice(GOOD_COMMENTS))
                break
            elif answer == "":
                print("Not sure?")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong!")
                print(random.choice(BAD_COMMENTS))
            else:
                print("That wasn't an option.")
                
                
            question_attempts -= 1
            print("The answer is ")
            

    #end of quiz
    print("Well done {}. You completed the quiz. Your final score was {}".format(name,score))

    # replay 
    play = input("Do you want to play again? ").lower()