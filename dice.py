import random
while True:
    user_input=input("Do you wanna roll the die(yes/no):").lower()
    if user_input=="yes":
        ans=random.randint(1,6)
        print("Die rolled to:",ans)
    elif user_input=="no":
        print("Had a great time see you soon!!!")
        break
    else:
        print("Enter yes or no")
