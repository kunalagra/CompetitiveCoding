#include <stdio.h>

int main(void) {
    long t;
    scanf("%ld",&t);
    if(t<=100000){
        while(t--){
            long long int n=0,x=0,k=0,sum=0;
            scanf("%ld %ld %ld",&n,&x,&k);
            if((x<=n)&&(k<=n)&&(n<=1000000000)){
            	if((x%k==0)||((n+1-x)%k==0)){
            		printf("YES\n");
            	}
            	else{
            		printf("NO\n");
            	}
           	}
        }
    }

	return 0;
}

