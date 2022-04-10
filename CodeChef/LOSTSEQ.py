t = int(input())
while (t!=0):
	n = int(input())
	nn =2*n
	b = list(map(int,input().strip().split()))[:nn]
	a= sum(b)
	if(a%2==0):
		print("YES")
	else:
		print("NO")
	t-=1
