# cook your dish here
from collections import Counter
for _ in range(int(input())):
	n = int(input())
	s = str(input())
	l1,l2=[],[]
	for x in range(n):
		a = l1 if x%2==0 else l2
		a.append(s[x])
	c1,c2 = Counter(l1),Counter(l2)
	f=0
	for i in c1:
		if c1[i]!=c2[i]:
			f=1
			break
	if f:
		print("NO")
	else:
		print("YES")