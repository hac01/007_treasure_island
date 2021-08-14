print('''    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure island")
print("A land full of mystries")
#print("Prove yourself to be agent 007 ")
#story line 'Hey As you know you are on a test to become agent 007 so choose left or right'
#if right then you are front of a lake what you want to do swim or use boat
#if swim oh no it was a private lake owned by a man .And he use to keep his sharks in .They were hungry from many days and the have eaten you .You died mission failed
#if boat you are front of a lake what you want to do swim or use boat
#one haha there a ghost and you died
#two Congratulations you were succesfull in your mission .You are now agent 007
choice1=input("Hey As you know you are on a test to become agent 007 so choose left or right \n").lower()

if choice1=="left":
  choice2=input("You are front of a lake what you want to do 'swim' or wait for the 'boat'\n").lower()
  if choice2=="boat":
    choice3=input("Oh you tooked the right decision .Now there are three doors 'red','yellow','blue' .Blue is my lucky color agent\n").lower()
    if choice3=="red":
        print("Haaaaa you took are really terible decision and you died")
    elif choice3=="yellow":
        print("Congratulations you are now agent 007 ")
    elif choice3=="blue":
        print("Beep You died .Game over ")
  else:
    print("Ohh Noo it was a private lake owned by a man .And he use to keep his sharks in it  .They were hungry from many days and the have eaten you .You died mission failed")
else:
    print("Better luck next time !")
