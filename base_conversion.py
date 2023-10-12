a = int(input("Enter numbers of words you want to add in the Dict: "))
k = list()
for i in range(a):
    b = input("Enter your string: ")
    k.append(b)
# k1 = dict()
# k.sort()
# k2 = 1
# for j in k:
#     k1[j] = k2
#     k2 += 1
# print(k1)
d = {"a" : 11 ,"b" : 12,"c" : 13,"d" : 14,"e" : 15,"f" : 16,"g" : 17,"h" : 18,"i" : 19,"j" : 20,"k" : 21,"l" : 22,"m" : 23,"n" : 24,"o" : 25,"p" : 26,"q" : 27,"r" : 28,"s" : 29,"t" : 30,"u" : 31,"v" : 32,"w" : 33,"x" : 34,"y" : 35,"z" : 36}


t1 = dict()
t2 = list()
t3 = list()

for i in k :
    s = 0
    t = 0
    for j in i :
        a1 = d[j]
        s = s + a1
        s = s * 100
        t += 1
    s = int(s / 100)
    t1[i] = s
    s = str(s)
    t2.append(s)

for i in t2 :
    i = str(i)
    p = len(i)
    t3.append(p)
b= max(t3)

for i,j in t1.items() :
    j = str(j)
    k1 = b - len(j)
    j = int(j)
    t1[i] = j * (10 ** k1)


print("\n\n" , t1 , "\n\n")


        
