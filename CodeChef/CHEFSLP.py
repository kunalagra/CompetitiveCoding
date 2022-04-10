# cook your dish here
test = int(input())
if (test<=10**3) and (test>=1):		
	while test >= 1:
		n, l, x = map(int, input().split())
		a = l*2
		if(a<=n):
			print(l*x)
		else:
			print((n-l)*x)
		test -= 1	
