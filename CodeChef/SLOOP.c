#include <stdio.h>

int main(void) {
    int t,m,s;
	scanf("%d",&t);
	int i;
	for(i=0;i<t;i++){
	    scanf("%d %d",&m,&s);
	    int j = 0;
	    j = m/s;
	    printf("%d\n",j);
	}
	
	return 0;
}

