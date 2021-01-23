#Create a user defined function to multiply all the numbers in a given list.
def numbers(a):
    t=1
    for x in a:
        t=t*x
    return t
print(numbers((52,25)))