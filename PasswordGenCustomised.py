import string , random


s1 = (list(string.ascii_lowercase))
s2 = (list(string.ascii_uppercase))
s3 = (list(string.digits))
s4 = (list(string.punctuation))


num = int(input("no.of password you wanna generate\n"))

for x in range (num) :
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    random.shuffle(s)


    len = int(input("Enter Your Password Length\n"))

    password = []
    password.extend(s1[:1])
    password.extend(s2[:1])
    password.extend(s3[:1])
    password.extend(s4[:1])
    password.extend(s[:len-4])


    random.shuffle(password)

    print("".join(password[:len]))





