test = int(input())
if (test<=10**3) and (test>=1):		
	while test >= 1:
		n = int(input())
		list1 = list(map(int,input().strip().split()))[:n]
		max = list1[0]
		count =0
		for i in list1:
			gt = 0
			lt = 0
			j=1
			for j in list1:
				if j <= i:
					lt += 1
				else:
					gt += 1
			if lt>gt:
				count +=1
		print(count)
		test -= 1	
