print ("Select your ride")
print ("1.bike")
print ("2.car")
choice= int(input("Enter your choice"))
if(choice==1):
    print("What type of bike?")
    print("1.scooty")
    print("2.scooter")
    choice2= int(input("Enter your choice"))
    if choice2==1:
        print("You have selected scooty")
    else:
        print("You have selected Scooter")
elif(choice==2):
        print("What type of car?")
        print("1.Sedan")
        print("2.SUV")
        choice3= int(input("Enter your choice"))
        if choice3==1:
           print("You have selected sedan")
        else:
           print("You have selected SUV")
else:
    print("Wrong choice")