#I can already tell this is going to be a goddamn rabbit hole of things that could be added.
#TBH I totally lost my place with what I was trying to do in this so I'm just submitting it and then I'm gonna go back and edit later.

import random
import math

#monster class
class Monster:
    def __init__(self):
        self.monsterNames=["Harpie","Goblin","Gremlin","Speed Demon","Werewolf"]
        self.thisMonster=random.choice(self.monsterNames)
        self.monsterHealth=random.randint(10,50)
        self.monsterCurrentHealth=self.monsterHealth
        self.monsterAttack=random.randint(5,15)
        self.monsterDefense=random.randint(5,15)
    
    def introMonster(self):
        print(f"Oh no, you've been attacked by a {self.thisMonster}! It has a health of {self.monsterCurrentHealth}/{self.monsterHealth}. Be careful!")
    
    def monsterBattleOptions(self,player):
        engage==True
        monsterChoice=random.randint(0,5)
        
        #code in an option for monster to flee later?
        # while engage==True and self.monsterCurrentHealth>=0:
        #     if monsterChoice%5==0:
        #         print("The monster chose to flee!")
        #         engage=False

#player class
class Player:
    def __init__(self,name):
        self.name = name
        self.attack = 10
        self.defense = 10
        self.overallHealth = 30
        self.currentHealth = 30
        self.distFromGoal = 100
    
    def printStats(self):
        print(f"Your current stats are:\nHealth: {self.currentHealth}/{self.overallHealth}\nAttack Power: {self.attack}\nDefense Ability: {self.defense}\nYou are currently {self.distFromGoal} travels from your goal.")
    
    def setupQuestion(self,question):
        correctAnswer = False
        
        while correctAnswer==False:
            answer1 = input(question)
            if answer1.lower()=="a":
                self.overallHealth+=10
                self.currentHealth+=10
                correctAnswer=True
            elif answer1.lower()=="b":
                self.defense+=5
                correctAnswer=True
            elif answer1.lower()=="c":
                self.attack+=5
                correctAnswer=True
            else:
                "I'm sorry, please answer with only your letter choice."
                
    def setupStats(self):
        questions = ["How do you wake up in the morning?\nA:Naturally, on my own.\nB:I burrito into a blanket and ignore the world.\nC:I'm just angry.\n",
        "What is your favorite of these colors?\nA:Green\nB:Blue\nC:Red\n",
        "Which animal do you most identify with?\nA:Sea lion\nB:Elephant\nC:Regular lion\n"]
        
        for each in questions:
            self.setupQuestion(each)
        
        print(f"Okay, we know a lot about you now, {self.name}.")
    
    def travel(self):
        print("Time to go.")
        travelDistance = random.randint(0,10)
        self.monsterEncounter(travelDistance)
        self.distFromGoal-=travelDistance
        print(f"You made it {travelDistance} travels. You have {self.distFromGoal} travels left to go.")
        
    def monsterEncounter(self, distance):
        if distance%3==0:
            newMonster = Monster()
            newMonster.introMonster()
            
            correctAnswer = False
            engage = True
            
            while correctAnswer==False and (newMonster.monsterCurrentHealth>0 or engage==False):
                decision=input(f"What do you want to do?\nA: Attack the {newMonster.thisMonster}!\nB: Flee!!!\n")
                if decision.lower()=="a":
                    self.playerAttack(newMonster)
                    correctAnswer==True
                elif decision.lower()=="b":
                    fleeChance = random.randint(0,6)
                    if fleeChance%2==0:
                        print("Got away safely!")
                        engage==True
                        correctAnswer==True
                    else:
                        print("Couldn't get away!")
                        correctAnswer==True
                else:
                    print("You must choose a or b to continue your travels.")
                    correctAnswer==False
    
    def playerAttack(self,newMonster):
        print("You attacked the beast.")
        damage=self.attack-int(newMonster.monsterDefense/2)
        newMonster.monsterCurrentHealth-=damage
        print(f"You dealth {damage}. The monster's health is now {newMonster.monsterCurrentHealth}/{newMonster.monsterHealth}.")

#global functions start here
def startAndSetup():
    print("Welcome to NotZelda!")
    username = input("What should we call you?\n")
    player1 = Player(username)
    print(f"Okay, welcome {player1.name}!")
    print("Let's find out more about what kind of adventurer you are.")
    player1.setupStats()
    player1.printStats()
    return player1

#actual game is here
player1=startAndSetup()
while player1.distFromGoal>=0:
    player1.travel()