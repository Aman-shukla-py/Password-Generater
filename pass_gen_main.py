import string
import random

#taking the things for password
n=int(input("Enter the length of the password: "))
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation

#making a list of charrecters
l=[]
l.extend(list(s1))
l.extend(list(s2))
l.extend(list(s3))
l.extend(list(s4))

#printing the password
random.shuffle(l)
print("Your passwor is:","".join(l[0:n]))