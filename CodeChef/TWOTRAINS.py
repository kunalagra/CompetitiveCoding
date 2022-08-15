# cook your dish here
for _ in range(int(input())):
    n  = int(input())
    l1 = list(map(int,input().split()))
    print(sum(l1)+max(l1))