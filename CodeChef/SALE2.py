t = int(input())
while (t!=0):
	n,x = map(int,input().split())
	a = round((n/3)%1,2)
	b = (n//3)*2
	if a == .33:
		a=1
	elif a == .67:
		a=2
	else:
		a=0
	print((a+b)*x)

	t-=1