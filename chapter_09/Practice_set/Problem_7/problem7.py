# Write a program to find out the line number where python is present from ques 6.


with open("line.txt") as f:
    lines=f.readlines()
linenum=1
for line in lines:
    if("Python" in line):
        print(f"Python is present in line number:{linenum}")
        break
    linenum+=1

else:
    print("Python is not present.") 
  