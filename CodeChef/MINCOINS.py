# cook your dish here
t = int(input())
while (t!=0):
	x = int(input())

	if x%10 == 5:
		print(x//10+1)
	elif x%10==0:
		print(int(x/10))
	else:
		print(-1)
	t-=1