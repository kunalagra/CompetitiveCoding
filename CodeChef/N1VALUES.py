test = int(input())
while test >= 1:
	n = int(input())
	if(n<=60) and (n>=1):
		a = (2**n)
		count =1
		print("1 ",end='')
		for i in range(1,n):
			print(f'{i} ',end='')
			count += i
		print(a-count)

	test -= 1