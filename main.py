score = 0

# Ask the user their name
name = input("Hello, what is your name? ")

# Welcome to the quiz
print ("This quiz is a stupid quiz",name)

# Question/Answers
answer1=input("Are you stupid? ")

if answer1.lower() == "yes":
 print("Correct!")
 score =+10000

else:
 print("Incorrect!")
 print("answer is yes")
 score =-10000

print("Your final score is", score)

# Thanks for playing
print("Thanks for playing")

