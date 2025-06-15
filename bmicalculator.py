height= int(input("Enter the height in cms"))
weight= int(input("Enter the weight in kgs"))
bmi= weight/(height/100)**2
print ("Your bmi is", bmi)
if bmi<=19:
    print ("You are underweight")
elif bmi<=25:
    print ("You are healthy")
elif bmi<=30:
    print ("You are over weight")
elif bmi<=35:
    print ("You are severely overweight")
elif bmi<=40:
    print ("You are obese")
else:
    print ("You are sereverly obese")