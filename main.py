import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is freindly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Wich cave will you go into? (1 or 2)')
        cave = input()

        return cave

def checkCave(chosenCave):
    print('You aproach the cave...')
    time.sleep(2)
    print('It is a dark and spooky...') 
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaw and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
       print('Gives you his treasure') 
    else:  
           print('Gobbles down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

 displayIntro()

 caveNumber = chooseCave()

 checkCave(caveNumber)

 print('Do you want to play again?  (yes or no)')
 playAgain = input() 