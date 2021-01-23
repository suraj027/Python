#Write a program to find the medicine bill.
d=int(input("Enter drug no. "))
dn=input("Enter drug name: ")
u=int(input("Enter number of units purchased: "))
r=int(input("Enter rate per unit: "))
p=input("Enter packing unit, press I=Injection, B=Bottle,T=Tablet: ")
if(p=="I"):
    h=(u*r*7.5)/100
    j=(h*7.5)/100
    l=(h+j)
    print("Discount on injection is 7.5%")
    print("Total amount payable: ",l)
elif(p=="B"):
    h1=(u*r*5)/100
    j1=(h1*7.5)/100
    l1=(h1+j1)
    print("Discount on bottle is 5%")
    print("Total amount payable: ",l1)
elif(p=="T"):
    h2=(u*r*2.5)/100
    j2=(h2*7.5)/100
    l2=(h2+j2)
    print("Discount on tablet is 2.5%")
    print("Total amount payable: ",l2)