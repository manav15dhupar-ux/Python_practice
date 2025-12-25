# Write a program using functions to find greatest of three numbers.

def great(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest.")
    elif(b>c and b>a):
        print(f"{b} is greatest.")
    else:
        print(f"{c} is greatest.")


great(2,3,4)
