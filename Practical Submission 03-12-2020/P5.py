#Create a user define function to calculate compound interest rate.
def cal(P,r,n,t):
    d=(r/100)
    a=(n*t)
    s=(P*1+d/n*a)
P=int(input("Enter Principle Amount: "))
r=int(input("Enter Interest Rate: "))
n=int(input("Enter the Number of Times that Interest is Compounded per unit 'Time': "))
t=int(input("Enter Time Period: "))
s=cal(P,r,n,t)
print("Compund Interest: ",s)    