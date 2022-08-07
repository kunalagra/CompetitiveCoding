# cook your dish here
t = int(input())

for x in range(t):
	a,b,n =map(int,input().split())
	if  a==b:
		print(0)
	else:
		c=a^b
		if c<n:
			print(1)
		elif c.bit_length()==n.bit_length() and n & (n-1):
			print(2)
		else:
			print(-1)