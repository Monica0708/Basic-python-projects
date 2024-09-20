import random
computer_wins=0
user_wins=0
pick=["snake","water","gun"]
while True:
    user_input=input("Enter snake,water or gun or 'q' to quit the game:").lower()
    if user_input=='q':
        print("See you next time")
        break
    if user_input not in pick:
        print("Enter valid input")
        continue
    random_number=random.randint(0,2)
    computer_input=pick[random_number]
    print("Computer picked",computer_input)
    if(user_input=="snake" and computer_input=="water"):
        print("You WON!!!")
        user_wins+=1
    elif(user_input=="gun" and computer_input=="snake"):
        print("Hurayyy!You WON")
        user_wins+=1
    elif(user_input=="water" and computer_input=="gun"):
        print("Great!You WON!!")
        user_wins+=1
    else:
        print("Computer WINS!!!")
        computer_wins+=1
print("Computer WON",computer_wins,"times")
print("User WON",user_wins,"times")
print("Had a great time with U SEE U SOON!!!!!")
        
