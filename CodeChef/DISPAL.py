t = int(input())

for x in range(t):
	n,x=map(int,input().split())
	s="abcdefghijklmnopqrstuvwxyz"
	res=''
	m=((n/2)+1) if n%2!=0 else (n/2)

	if x>m:
		print(-1)
	else:
		res+=s[0]*int(m-(x-1))
		for letter in s[1:x]:
			res+=letter
		a=res[::-1]
		if n%2!=0:
			a=a[1:]
		res+=a
		print(res)
