speed1= 10
speed2= 20
speed3= 30
average= (speed1+speed2+speed3)/3
print("Average=", average)
if speed1<average:
    print("Cyclist1 is slower than average")
elif speed2<average:
    print("Cyclist2 is slower than average")
elif speed3<average:
    print ("Cyclist3 is slwoer than average")
else:
    print("Invalid input")