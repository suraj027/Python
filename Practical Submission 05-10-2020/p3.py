#Write a program to accept marks of a quiz obtained by one student.
m=int(input("Enter quiz marks: "))
if(m>9):
    print("Result: Excellent")
elif(m>7):
    print("Result: Very good")
elif(m>5):
    print("Result: Good")
elif(m==4):
    print("Result: Average")
else:
     print("Result: Poor")