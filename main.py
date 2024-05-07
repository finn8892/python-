score = 0

# Ask the user their name
name = input("Hello, what is your name? ")

# Welcome to the quiz
print ("This quiz is a stupid quiz",name)

# Question/Answers
answer1=input("Are you stupid? ")

if answer1=="yes" or answer1 == "yup":
 print("Correct!")
 score =+10000

else:
 print("Incorrect!")
 print("answer is yes")
 score =-10000

#question2
question2=input("who has the most albums")
a="drake"
b="kanye west"
c="kendrick lamar"
d="yuno miles"
answer2=input("{}/nA.{}B.{}C.{}D.{}}"format(question2,a,b,c,d)).lower()

if answer2 == b or answer2== "b":
 print("correct")
 score+=10000

else:
 print("incorrect")
score=-100000


# Thanks for playing
print("good job{}.you have completed the quiz. your final score was{}".format(name,score))

