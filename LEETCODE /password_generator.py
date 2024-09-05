import string 
import random
if __name__=="__main__":
    # s1=string.ascii_lowercase
    # s2=string.ascii_uppercase
    # s3=string.digits
    # s4=string.punctuation
    s1=string.printable

    plen=int(input("enter the password length u want to set\n"))
    s=[]
    s.extend(s1)
    # s.extend(s2)
    # s.extend(s3)
    # s.extend(s4)
    # print(s)
    random.shuffle(s)
    # print(s)
    print("".join(random.sample(s,plen)))
    # print("".join(s[0:plen]))

