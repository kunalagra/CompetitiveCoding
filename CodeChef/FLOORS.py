# cook your dish here
t = int(input())

for x in range(t):
	x,y=map(int,input().split())
	x = x/10 if x%10==0 else x/10+1
	y = y/10 if y%10==0 else y/10+1
	print(abs(int(x)-int(y)))
