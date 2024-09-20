import time
def countdown(seconds):
    print("The countdown STARTS NOW!!!")
    for i in range(seconds,0,-1):
        print(i)
        time.sleep(1)
    print("The scheduled time has been successfully completed!")
    print("Hope it was helful and made your time productive!")
    print("See you soon!!")
seconds=int(input("Enter how many seconds you want?"))
countdown(seconds)
