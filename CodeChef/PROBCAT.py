# cook your dish here
test = int(input())
if (test<=50) and (test>=1):		
	while test >= 1:
		n = int(input())
		var =""
		if (n<=300) and (n>=1):
			if(n<100):
				var="Easy"
			elif (n<200):
				var="Medium"
			elif (n<=300):
				var ="Hard"
			print(var)
		test -= 1