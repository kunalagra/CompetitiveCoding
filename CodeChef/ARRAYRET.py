t = int(input())

for _ in range(t):
	n = int(input())
	b = list(map(int, input().strip().split()))
	s = sum(b)//(n+1)
	a=[]
	for x in b:
		a.append(x-s)
	print(*a)