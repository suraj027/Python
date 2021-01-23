#Create a user defined function to sum all the numbers in a given list.
def numbers(a):
    t=0
    for x in a:
        t=t+x
    return t
print(numbers((52,25,65,36,45,78,45,65,12)))