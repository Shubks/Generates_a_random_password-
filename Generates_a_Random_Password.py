#importing module
import random

#all characters
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha="abcdefghijklmnopqrstuvwxyz"
nums="0123456789"
signs="!@#$%&"
a=int(input("Enter length of password: "))
for i in range(0,a):
    print(random.choice(ALPHA + alpha + nums + signs), end="")
