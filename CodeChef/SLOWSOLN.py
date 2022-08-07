t = int(input())

for x in range(t):
	mT,mN,sN=map(int,input().split())
	ans=0
	while(mT and sN):
		mT-=1
		if(sN>=mN):
			ans+=pow(mN,2)
			sN-=mN
		else:
			ans+=pow(sN,2)
			break
	print(ans)