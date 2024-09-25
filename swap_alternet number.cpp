//for even len:-  1,2,3,4,5,6 
//      result:-  2,1,4,3,6,5 
//for odd len:-  1,2,3,4,5,6,7
//      result:- 2,1,4,3,6,5,7



#include<iostream>
using namespace std;

void print(int a[],int n){
	int i;
	for(i=0;i<n;i++){
		cout<<" "<<a[i];
	}
	cout<<endl;
}
void swap_alternet(int a[],int n){
	int i;
	for(i=0;i<n;i+=2){
		if(i+1<n){
			int temp=a[i];
		    a[i]=a[i+1];
		    a[i+1]=temp;	
		}
	}
}
			
			
int main(){
	int a[]={2,11,4,6,3,7,8};
	int n=sizeof(a)/sizeof(a[0]);
	print(a,n);
	swap_alternet(a,n);
    print(a,n);
    return 0;
}
