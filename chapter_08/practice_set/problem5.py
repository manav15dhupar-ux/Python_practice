# Write a python function which converts inches to cms.

def inch(i):
    c=i*2.54
    return c

i=float(input("Enter the value:"))

print(f"{i} is {inch(i)} cm")