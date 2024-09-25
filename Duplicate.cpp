//You are given an array ARR oof size 'N' containing 
//each number between 1 and 'N-1' at least once. 
//There is a single integer value that is present in the array twice.
// Your task is to find the duplicate integer.

#include<iostream>
using namespace std;

int duplicate(int a[], int n){
	int i;
	int sum=0;
	for(i=0;i<n;i++){
		sum=sum^a[i];
	}
	for(i=1;i<n;i++){
		sum=sum^i;
	}
	return sum;
}


int main(){
	int a[]={1,2,3,5,3,4};
    cout<<duplicate(a,6);
	return 0;
}
