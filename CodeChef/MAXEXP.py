for _ in range(int(input())):
    n= int(input())
    l=input()
    l2=["0","1",'2','3','4','5','6','7','8','9']
    a = dict(zip(l2,[0]*10))
    a['+']=0
    a['-']=0
    for x in l:
        a[x]+=1
    dig = n-(a['+']+a['-'])
    ans=""
    i=9
    while(dig-(a['+']+a['-'])):
        if(a[str(i)]==0):
            i-=1
            continue
        ans+=str(i)
        a[str(i)]-=1
        dig-=1
    
    while(a['+']):
        if(a[str(i)]==0):
            i-=1
            continue
        ans+="+"
        ans+=str(i)
        a[str(i)]-=1
        a['+']-=1
    while(a['-']):
        if(a[str(i)]==0):
            i-=1
            continue
        ans+="-"
        ans+=str(i)
        a[str(i)]-=1
        a['-']-=1
    print(ans)