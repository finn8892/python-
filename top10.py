BIGGEST_ANIMALS_ANSWERS=["blue whale","african elephant","giraffe","hippopotamus","polar bear","saltwater crocodile","ostrich","grizzly bear","giant squid","whale shark"]
#------Functions-------
def getLives():
    while True:
        lives = input("how many chances do you want")
        try:
            lives=int(lives)
            if lives >=0:
                return lives 
            else:
                print("please choose a positive number")
        except:
            print("that wasn't an number")

#welcome user and introduce to the quiz
def intro():
    #ask the user their name
    name=input("whats your name")

    #greet the user and introduce the quiz
    print("welcome to the quiz",name)
    ("This quiz is about the ten largest animals in the world. Can you name them")

#-----MAIN CODE-------

intro()
lives = getLives()
score=0
while lives >0:
    answer=input("whats the ten largest animals")