t = int(input())

for x in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	odd_ctr = len(list(filter(lambda x: (x&1) , l)))
	if min(l)==1:
		print("CHEF")
	elif odd_ctr%2==0:
		print("CHEFINA")
	else:
		print("CHEF")