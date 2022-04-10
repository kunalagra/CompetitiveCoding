#include <stdio.h>
#include<stdio.h>

int main() {
    int t, n, a, b;
    scanf("%d", &t);
    int i;
    if (t<=100){
    while(t--){
        long anu = 0, sar = 0;
        scanf("%d %d %d", &n, &a, &b);
        if (n<=100 && a<=1000000000 && b<=1000000000){
        for (i = 0; i < n; i++) {
            char getstrings[100],fc;
            scanf("%s",getstrings);
            fc = getstrings[0];
            if ((fc == 'E') || (fc == 'Q') || (fc == 'U') || (fc == 'I') || (fc == 'N') || (fc == 'O') || (fc == 'X')) {
                sar = sar + a;
            } else {
                anu = anu + b;
            }
        }
    }
        if (anu < sar) {
            printf("SARTHAK\n");
        }
        else if (anu > sar) {
            printf("ANURADHA\n");
        }
        else {
            printf("DRAW\n");
        }
    }
}
    return 0;
}
