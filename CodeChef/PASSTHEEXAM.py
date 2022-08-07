# cook your dish here
t = int(input())

for x in range(t):
	l=list(map(int,input().split()))
	if min(l)<10 or sum(l)<100:
		print("FAIL")
	else:
		print("PASS")
