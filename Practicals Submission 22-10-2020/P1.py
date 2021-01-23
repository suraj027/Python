#Print multiplication for a given number using while loop.
print("Enter number to get multiplication table: ")
n=int(input(" "))
i=0
while i<=9:
    i=i+1
    m=n*i
    print(n,"x",i,"=",m)
