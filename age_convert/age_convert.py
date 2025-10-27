user_age = int(input("Enter your Age for convert: "))
choice = int(input("what you want to know?" \
"1- Hour" \
"2- Minute" \
"3- Second" \
": "))
def Convert_Hour():
    hour = user_age * 365 * 24
    print("Your age in hours is:", hour)
def Convert_Minute():
    Minute = user_age * 365 * 24 * 60
    print("Your age in minutes is:", Minute)

def Convert_Second():
    Second = user_age * 365 * 24 * 60 * 60
    print("Your age in Second is:",Second)
    
if (choice == 1):
    Convert_Hour()
elif(choice == 2):
    Convert_Minute()
elif(choice == 3):
    Convert_Second()
