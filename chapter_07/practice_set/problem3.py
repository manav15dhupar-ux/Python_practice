# Write a program to find the sum of first n natural numbers using while loop.

num=int(input("Enter a range:"))

i=1
s=0

while i<=num:
    s=s+i
    i+=1

print(f"The sum of numbers from 1 to {num} is {s} .")