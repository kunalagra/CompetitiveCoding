t = int(input())

for _ in range(t):
	x = int(input())
	s=0
	if x>99:
		s=int(x/100)
	s+=int(x%100)
	if s>10:
		print(-1)
	else:
		print(s)