import random

a = ""
k1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
b = int(input("Enter length of string: "))


for i in range(b):
    k = random.randint(0,25)
    a += k1[k]

print(a)