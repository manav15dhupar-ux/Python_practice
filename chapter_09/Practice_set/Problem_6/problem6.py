# Write a program to mine a log file and find out whether it contains 'python'.

with open("log.txt","r") as f:
    content=f.read()
py="Python"
if(py in content or py.lower() in content):
    print("Python is present")

else:
    print("Python is not present.")