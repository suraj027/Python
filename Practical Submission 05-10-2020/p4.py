#Program to calculate eletricity bill.
n=int(input("Enter customer number: "))
present=int(input("Enter present reading: "))
past=int(input("Enter past reading: "))
con=(present-past)
if(con>=0 and con<=200):
    r1=(con*2.5)
    print("Total bill: ",r1)
elif(con>=201 and con<=400):
    r2=(con*3+500)
    print("Total bill: ",r2)
elif(con>=401 and con<=600):
    r3=(con*5+1100)
    print("Total bill: ",r3)
elif(con>600):
    r4=(con*8.5+2100)
    print("Total bill: ",r4)