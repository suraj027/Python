#Program to calculate bonus for an employee.
s=int(input("Enter your salary to calculate bonus: "))
if(s<2000):
    c1=(s*5)/100
    b1=(s+c1)
    print("Bonus: ",b1)
elif(s>2000, s<5000):
    c2=(s*7)/100
    b2=(s+c2)
    print("Bonus: ",b2)
elif(s>5000,s<7000):
    c3=(s*9)/100
    b3=(s+c3)
    print("Bonus: ",b3)
elif(s>7000):
    c4=(s*12)/100
    b4=(s+c4)
    print("Bonus: ",b4)