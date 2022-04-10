t= int(input())
e=1
while t!=0:
	n= int(input())
	s = list(map(int,input().split()))
	s.sort()
	count=0
	for x in s:
		if count<x:
			count+=1
	print(f'Case #{e}: {count}')
	e+=1
	t-=1