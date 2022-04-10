t= int(input())
e=1
while t!=0:
	p1 = list(map(int,input().split()))
	p2 = list(map(int,input().split()))
	p3 = list(map(int,input().split()))
	c = min(p1[0],p2[0],p3[0])
	m = min(p1[1],p2[1],p3[1])
	y = min(p1[2],p2[2],p3[2])
	k = min(p1[3],p2[3],p3[3])
	q=""
	s= c+m+y+k
	if s==1000000:
		q=" "+str(c)+" "+str(m)+" "+str(y)+" "+str(k)
	elif s>1000000:
		l = [c,m,y,k]		
		z=s-1000000
		i=1
		while z!=0:
			re =int(z/i)
			v = max(l)
			if re<v:
				w=l.index(v)
				l[w] = v-re
				z-=re
				i=1
			else:
				i+=1		
		
		for ele in l:
			q=q+" "+str(ele)
	else:
		q=" IMPOSSIBLE"
	print(f'Case #{e}:{q}')
	e+=1
	t-=1