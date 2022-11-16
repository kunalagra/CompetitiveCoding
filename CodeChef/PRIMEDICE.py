def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                print("Bob")
                return
        print("Alice")
        return
    else:
        print("Bob")
        return
for x in range(int(input())):
    a,b = map(int,input().split())
    isprime(a+b)

