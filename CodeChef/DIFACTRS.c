#include <stdio.h>

int main(void) {
    int n,i,j=0;
    long ft[10000000]= {};
    if (n<=1000000){
	// your code goes here
	scanf("%d",&n);
	
	for(i=1;i<=n;i++){
	    if(n%i==0) {
	        ft[j] = i;
	        j++;
	    }
	}
    printf("%d\n",j);
    
    for(int k=0;k<j;k++){
        printf("%ld ",ft[k]);
        
    }
    }
	return 0;
}

