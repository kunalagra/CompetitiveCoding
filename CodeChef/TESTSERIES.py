test = int(input())
if (test<=1000) and (test>=1):		
	while test >= 1:		
		stri = str(input())
		list1 = stri.split()
		list1 = [int(i) for i in list1]
		india = draw = england = 0
		flag = False
		for i in list1:
			if i == 0:
				draw += 1
			elif i == 1:
				india += 1
			elif i == 2:
				england += 1
			else:
				flag = True
				break
		if flag:
			pass
		elif (india == england):
			print("DRAW")
		elif (india>england):
			print("INDIA")
		elif (england>india):
			print("ENGLAND")
		test -= 1
