#Write a Python program to remove an item from a tuple.
tuple1=("Red","Green", "White", "Black", "Pink", "Yellow")
l=list(tuple1)
l.remove("Green")
t=tuple(l)
print(t)