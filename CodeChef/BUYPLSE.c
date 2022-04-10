#include <stdio.h>

int main(void) {
	int a,b,x,y,tc;
	scanf("%d %d %d %d", &a, &b, &x, &y);
	if((a<=1000)&&(b<=1000)&&(x<=1000)&&(y<=1000)){
	tc = ((a*x)+(b*y));
	printf("%d",tc);
	}
	return 0;
}

