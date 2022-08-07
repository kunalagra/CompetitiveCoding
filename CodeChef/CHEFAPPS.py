t = int(input())

for _ in range(t):
	s,x,y,z = map(int, input().split())
	f=s-(x+y)
	if z-f>0:
		if z-f<=x or z-f<=y:
			print(1)
		else:
			print(2)
	else:
		print(0)