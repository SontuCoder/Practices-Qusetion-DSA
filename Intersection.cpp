//You are given two array 'A' and 'B' of size 'N','M' respectively.
//Both these are sorted in non-decreasing order. You have to find the
// intersection of these two arrays.
// A=[1,2,2,3,4,5,5,5]
// B=[2,5,5,6,7]
// ans:- [2,5,5]

#include<iostream>
using namespace std;

void print(int a[], int n){
	int i;
	for(i=0;i<n;i++){
		cout<<" "<<a[i];
	}
	cout<<endl;
}

void inter(int a[], int n, int b[], int m){
	int c;
	print(a,n);
	print(b,m);
	if(n>m){
		c=m;
	}else{
		c=n;
	}
	int in[c],i=0,j=0,k=0;
	while(j<n && k<m){
		if(a[j]>b[k]){
			k++;
		}else if(a[j]<b[k]){
			j++;
		}else{
			in[i]=a[j];
			j++;
			k++;
			i++;
		}
	}
	print(in,i);
}

int main(){
	int A[]={1,2,2,3,4,5,5,5};
    int B[]={2,5,5,6,7};
    inter(A,8,B,5);
}
