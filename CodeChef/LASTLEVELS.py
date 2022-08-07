import math
for _ in range(int(input())):
	x,y,z=map(int,input().split())
	t = x*y + ((math.ceil(x/3)-1)*z)
	print(t)