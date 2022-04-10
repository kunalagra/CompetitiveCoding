t = int(input())
while (t!=0):
	n,x = [int(x) for x in input().split()]  
	a = list(map(int,input().strip().split()))[:n]
	max=x
	sum=x
	for i in a:
		sum+=i
		if(sum>max):
			max=sum
	print(max)
	t-=1
