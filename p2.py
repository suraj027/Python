#Write a program to calculate electricity bill. Input customer number, past reading, present reading, and customer type. Customers are of two types: I(Industrial) and R(Regular). For industrial customers, rate per unit is Rs. 10 while for regular customers; rate per unit is Rs. 6.5. Print the bill amount in appropriate format.
cn=int(input("Enter customer number: "))
p=int(input("Enter past reading: "))
pr=int(input("Enter present reading: "))
ct=input("Type of customer, press I for Industrial customer or R for Regular customer: ")
if (ct=="I"):
    a1=(pr-p)*10
    print("Your total amount for industrial customer: ",a1)
elif(ct=="R"):
    a2=(pr-p)*6.5
    print("Your toal amount for regular customer: ",a2)