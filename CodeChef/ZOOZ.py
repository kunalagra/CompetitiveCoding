# cook your dish here
t = int(input())

for x in range(t):
	n = int(input())
	if n%2==0:
		s = "1" + "0"*(n-2)+"1"
	else:
		s= "10"*int(n/2)+"1"
	print(s)
