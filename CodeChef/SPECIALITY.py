for _ in range(int(input())):
    l = list(map(int,input().split()))
    s = ["Setter", "Tester","Editorialist"]
    print(s[l.index(max(l))])