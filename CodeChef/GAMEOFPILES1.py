t = int(input())

for x in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	if (1 in l) or sum(l)%2!=0:
		print("CHEF")
	else:
		print("CHEFINA")