for _ in range(int(input())):
    s = input()
    v = {"a","e","i","o","u"}
    c = 0
    f = False
    for x in s:
        if x in v:
            c+=1
            if c>2:
                f=True
                break
        else:
            c=0
    ans = "Happy" if f else "Sad"
    print(ans)