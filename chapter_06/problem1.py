# Write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=int(input("Enter a number:"))

if(a>b and a>c and a>d):
    print(f"{a} is greater")
elif(b>a and b>c and b>d):
    print(f"{b} is greater")
elif(c > b and c > d):
    print(f"{c} is greater")
else:
    print(f"{d} is greater")

