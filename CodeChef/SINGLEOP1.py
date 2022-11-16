for _ in range(int(input())):
    n = int(input())
    a1 = input()
    cnt=0
    for x in a1:
        if x=='0':
            break
        else:
            cnt+=1
    print(cnt)