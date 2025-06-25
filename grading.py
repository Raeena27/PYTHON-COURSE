print("Enter the marks of five subjects")
science= int(input())
maths= int(input())
english= int(input())
socialscience= int(input())
economics= int(input())
total= science+maths+english+socialscience+economics
avg= total/5
if avg>=91 and avg<=100:
    print ("Your grade is A1")
elif avg>=81 and avg<91:
    print ("Your grade is A2")
elif avg>=71 and avg<81:
    print ("Your grade is B1")
elif avg>=61 and avg<71:
    print ("Your grade is B2")
elif avg>=51 and avg<61:
    print ("Your grade is C1")
elif avg>=41 and avg<51:
    print ("Your grade is C2")
elif avg>=31 and avg<41:
    print ("Your grade is D1")
elif avg>=21 and avg<31:
    print ("Your grade is D2")
elif avg>=11 and avg<21:
    print ("Your grade is E1")
else:
    print ("Fail")