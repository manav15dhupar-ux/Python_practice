# 2. Write a program to find out whether a student has passed or failed if it reqyires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


m=float(input("ENter your maths marks:"))
e=float(input("ENter your english marks:"))
s=float(input("ENter your science marks:"))

mp=(m/100)*100
ep=(e/100)*100
sp=(s/100)*100

tot=(m+e+s)
tot_per=(tot/300)

if(tot_per>=40):
    print(f"Your total percentage is {tot_per:.0%} more than 40 also you are ")
    if(mp>=33):
        print("pass in maths")
    if(ep>=33):
        print("pass in english")
    if(sp>=33):
        print("pass in science")

else:
    print(f"You fail ; better luck next time, you score {tot_per}")



    


