t = int(input())

for _ in range(t):
	n = int(input())
	b = list(map(int, input().strip().split()))
	e=0
	a=[]
	for x in b:
		if x%2==0:
			e+=1
			temp=x
			c=0
			while temp%2==0:
				c+=1
				temp//=2
			a.append(c)
	o = (2*n)-e
	if o>=e:
		print(o-n)
	else:
		a=sorted(a)
		print(sum(a[:e-n]))
