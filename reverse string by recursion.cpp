//reverse  string by ricursion:

#include<iostream>
using namespace std;

void print(char a[],int n){
	if(n==0){
		return;
	}
	cout<<a[0];
	print(a+1,n-1);
	cout<<endl;
}

void reverse(char a[],int n,int i){	
    if(i<n){
    	char b=a[i];
    	a[i]=a[n];
    	a[n]=b;
    	reverse(a,n-1,i+1);
	}	
}
int main(){
	char s[]="abcdef";
	print(s,6);
	reverse(s,5,0);
	print(s,6);


}
