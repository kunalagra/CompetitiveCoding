# cook your dish here
import math
for _ in range(int(input())):
	n = int(input())
	s = str(input())
	c=0
	s1 = {'a','e','i','o','u'}
	for x in s:
		if x in s1:
			c=0
		else:
			c+=1
			if c>3:
				break
	if c>=4:
		print("NO")
	else:
		print("YES")
