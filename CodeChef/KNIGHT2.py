# cook your dish here
for _ in range(int(input())):
	l=list(map(int,input().split()))
	if (abs(l[0]-l[1])+abs(l[2]-l[3]))%2==0:
		print("YES")
	else:
		print("NO")
