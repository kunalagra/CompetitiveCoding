t = int(input())

for _ in range(t):
	n, x = map(int, input().split())
	a = list(map(int, input().strip().split()))
	br = False
	for i in range(n-1):
		if a[i]>a[i+1]:
			if a[i]+a[i+1]>x:
				br=True
				break
			else:
				a[i], a[i+1] = a[i+1], a[i]
	if br:
		print("NO")
	else:
		print("YES")

