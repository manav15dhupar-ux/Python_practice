# Write a program to find whether a given username contains less than 10 characters or not.

user=input("ENter your username:")
user_len=len(user)

if(user_len>=10):
    print("The user name contains more than 10 characters")
    print(f"Total character are {user_len}")

elif(user_len==0):
    print("There are 0 characters in username")
    print(f"Total character are {user_len}")


else:
    print("The username have less than 10 characters")
    print(f"Total character are {user_len}")