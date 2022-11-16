for _ in range(int(input())):
    i = int(input())
    m = i//2
    s = input()
    if s[:m]==s[m:]:
        print("YES")
    else:
        print("NO")