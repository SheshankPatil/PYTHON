

pasparts=(('and','&'),('a','@'),('s','$'),('o','0'))

def securepassword(password):
    for a,b in pasparts:
        password=password.replace(a,b)
    return password 


password=input("enter your password:")
password=password.lower()
password=securepassword(password)
print(f"your new password is {password}")