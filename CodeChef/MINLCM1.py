test = int(input())
if (test<=10**5) and (test>=1):		
	while test >= 1:
		x, y = map(int, input().split())
		if (x>=1 and 10**8>=x) and (y>=2 and 10**8>=y):
			a = x*y
			min1 = 2*x
			max1 = a*(a-1)
			print(f'{(min1)} {(max1)}')
		test -= 1
