#include <bits/stdc++.h>
using namespace std;

#define lld long long int
int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	lld t=0, n=0;
	cin>>t;
	while (t--){
	    cin>>n;
		lld a = n-2;
		cout<<(a*(a+1))+1<<"\n";
	}
    return 0;
}