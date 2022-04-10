test = int(input())
if (test<=10**3) and (test>=1):		
	while test >= 1:
		a,b,p,q = map(int, input().split())
		if (10**9 >= (a and b and p and q)) and (1 <= (a and b and p and q)):
			if (p%a==0) and (q%b==0):
				d = int(abs((p/a) - (q/b)))
				if (d==1) or (d==0) :
					print("YES")
				else:
					print("NO")
			else:
				print("NO")		
		test -=1