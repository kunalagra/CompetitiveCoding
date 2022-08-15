# cook your dish here
for _ in range(int(input())):
    x = int(input())
    disc = 0
    if x<=100:
        pass
    elif x<=1000:
        disc = 25
    elif x<=5000:
        disc = 100
    else: 
        disc=500
    
    print(x-disc)