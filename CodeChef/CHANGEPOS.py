t = int(input())

for _ in range(t):
	x1,y1,x2,y2 = map(int, input().split())
	if x1==x2 or y1==y2:
		print(2)
	else:
		print(1)