#An electronic component vendor supplies three products: transistors, resistors and capacitors. The vendor gives discount of 10% on orders for transistors if order is for more than Rs. 1000. On order of more than Rs. 500 for resistors, a discount of 5% id given, and a discount of 10% is given on order for capacitors of value more than Rs. 2000. Write a Program that reads the product and the order amount and prints the net amount the customer is required to pay after discount.
t=int(input("Enter the price of the transistors: "))
r=int(input("Enter the price of the resistors: "))
c=int(input("Enter the price of the capacitors: "))
tt=(t+r+c)
if(t>1000):
    d1=(t*10)/100
    tt1=(t-d1)
    print("Price of the transistors after discount: ",tt1)
if(r>500):
    d2=(r*5)/100
    tt2=(r-d2)
    print("Price of the resistor after discount: ",tt2)
if(c>2000):
    d3=(c*10)/100
    tt3=(c-d3)
    print("Price of the capacitors after discount: ",tt3)
print("Total amount before discount: ",tt)
a=(tt1+tt2+tt3)
print("Total amount after discount: ",a)