#include <iostream>
using namespace std;
#define li long long int

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    li n,k,t,total=0;
    cin>>n>>k;
    if((n<=10000000)&&(k<=10000000)){
        while(n--){
            cin>>t;
            if(t%k==0){
                total++;
            }
        }
        cout<<total;
    }
    return 0;
}