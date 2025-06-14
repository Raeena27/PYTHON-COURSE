originalamount= int(input("Enter the original amount"))
Saleamount= int(input("Enter the sale amount"))
if Saleamount>originalamount:
    amount= Saleamount-originalamount
    print ("Total profit is", amount)
else: print ("Loss")