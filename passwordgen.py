import string
import random


s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

len = int(input("Enter Length Of Your Password : "))

password = random.choices(s,k=len)


print("".join(password))