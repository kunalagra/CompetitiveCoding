t = int(input())

for x in range(t):
	n,k=map(int,input().split())
	n1 = int(n/5) if n%5==0 else int(n/5)+1
	k1 = int(k/5) if k%5==0 else int(k/5)+1
	print(n1-k1)