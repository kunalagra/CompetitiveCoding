# cook your dish here
t = int(input())
while (t!=0):
	n,x,y = map(int,input().split())
	s = str(input())
	if '1' not in s:
		print(0)
	elif '0' not in s:
		print(0)
	elif x>y:
		print(y)
	else:
		print(x)
	t-=1