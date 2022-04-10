t= int(input())
e=1
while t!=0:
	r,c = map(int,input().split())
	r= r*2+1
	c= c*2+1
	print(f'Case #{e}:')
	e+=1
	for x in range(r):
		s=""
		for y in range(c):
			if x%2==0:
				if x==0 and y==0:
					s+="."
				elif x==0 and y==1:
					s+="."
				elif y%2==0:
					s+="+"
				else:
					s+="-"
			else:
				if x==1 and y==0:
					s+="."
				elif x==1 and y==1:
					s+="."
				elif y%2==0:
					s+="|"
				else:
					s+="."
		print(s)
	t-=1