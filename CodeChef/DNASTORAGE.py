t = int(input())

for x in range(t):
	l=int(input())
	s=str(input())
	res=""
	for x in range(0,len(s),2):
		if s[x:x+2]=="00":
			res+='A'
		elif s[x:x+2]=="01":
			res+='T'
		elif s[x:x+2]=="10":
			res+='C'
		else:
			res+='G'
	print(res)