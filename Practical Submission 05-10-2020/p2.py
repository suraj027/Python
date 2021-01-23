#Write a program to calculate total salary of an employee.
s=int(input("Enter basic salary: "))
if(s<10000):
    d1=(s*10)/100
    t1=(s+d1+500)
    print("Salary: ",t1)
elif(s>10000, s<15000):
    d2=(s*8)/100
    t2=(s+d2+300)
    print("Salary: ",t2)
elif(s>15000, s<25000):
    d3=(s*6)/100
    t3=(s+d3+250)
    print("Salary: ",t3)
elif(s>25000):
    d4=(s*4)/100
    t4=(s+d4)
    print("Salary: ",t4)