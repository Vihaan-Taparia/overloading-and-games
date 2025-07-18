import random

class Fruitquiz:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','dragonfruit':'purple','mango':'yellow','banana':'yellow'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer=input()
            if(user_answer.lower()==color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option=int(input('enter 0,if u want to play again else enter 1:'))
            if(option):
                break
print("Welcome to the one and only fruit quiz")
fq=Fruitquiz()
fq.quiz()

            