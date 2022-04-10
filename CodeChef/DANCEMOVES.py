test = int(input())
if (test<=10**3) and (test>=1):		
	while test >= 1:
		x, y = map(int, input().split())
		if (x>=-10**3 and 10**3>=x) and (y>=-10**3 and 10**3>=y):
			if (x<y):	
				diff = y-x
				div = diff//2
				if (diff%2==0):
					print(f'{int(div)}')
				else:
					print(f'{int(div+2)}')
			else:
				diff = x-y
				print(f'{int(diff)}')
		test -= 1