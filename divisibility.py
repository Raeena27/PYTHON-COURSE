num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
if num2==0:
    print("Division by 0 is not allowed")
elif num1%num2==0:
    print(num1, "Is divisible by", num2)
else:
    print(num1, "Is not divisible by", num2)