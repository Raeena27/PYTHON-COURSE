a= input("Do you have a medical condition? Y or N")
attendance= int(input("Enter the attendance of the student"))
if a=='Y': 
    print("You are allowed")
else:
    if attendance>=75:
        print("Allowed")
    else:
        print ("Not allowed")