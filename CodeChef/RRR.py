test = int(input())
if (test<=10**5) and (test>=1):		
	while test >= 1:
		x, y = map(int, input().split())
		a = ((2*x)-(y+1))//2
		print(f'{2*a}')
		test -= 1