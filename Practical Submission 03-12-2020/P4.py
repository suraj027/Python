#Create a user defined function to calculate simple interest.
def cal(p,r,t):
    s=(p*t*r)/100
    return s
p=int(input("Enter Principle Amount: "))
r=int(input("Enter Interest Rate: "))
t=int(input("Enter Time Period: "))
s=cal(p,r,t)
print("Simple Interest: ",s)