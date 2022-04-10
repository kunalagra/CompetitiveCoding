test = int(input())
if test<=1000:		
	while test >= 1:		
		stri = str(input())
		flag=1
		for i in stri:
			if i == "7":
				flag =0
				print("YES")
				break
		if flag:
			print("NO")
		test -= 1
