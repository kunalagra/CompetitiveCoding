#include <iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    if(t<=1000){
        while(t--){
            int x=0,a=0,b=0,sum=0;
            cin>>x>>a>>b;
            if((31<=x<=40)&&(101<=a<=120)&&(1<=b<=5)){
                sum = (a + ((100-x)*b))*10;
                cout<<sum<<endl;
            }
        }
    }
    return 0;
}