#Write a program in Python to convert decimal number to binary number creating user defined function.
def dtob(num):
    if num > 1:
        dtob(num // 2)
    print(num % 2,)
number=int(input("Enter decimal number: "))
dtob(number)