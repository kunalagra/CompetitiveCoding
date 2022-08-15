from math import sqrt
# cook your dish here
for _ in range(int(input())):
    x = int(input())
    s = "NO"
    for a in range(1,int(sqrt(x))):
        if ((x-(2*a))/(2+a)).is_integer():
            s = "YES"
            break
    print(s)
