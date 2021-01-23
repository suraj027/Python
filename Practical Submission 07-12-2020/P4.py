#Write a program in Python to check a given number is even or odd creating user defined function.
def check(n):
    oe=n%2
    if oe>0:
        print("Entered number is odd")
    else:
        print("Entered number is even")
num=int(input('Enter a number: '))
check(num)