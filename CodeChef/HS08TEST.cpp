#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float y,sum=0.00,balance=0.00; int x;
    cin>>x>>y;
    if((0<x<=2000)&&(0<=x<=2000)){
        if(x%5==0){
            sum = x + 0.50;
            if(sum<=y){
                balance=(float)y-sum;
                cout<<fixed << setprecision(2)<<balance;
            }
            else{
                cout<<fixed << setprecision(2)<<y;
            }
        } else{
            cout<<fixed << setprecision(2)<<y;
        }

    }
    
    return 0;
}