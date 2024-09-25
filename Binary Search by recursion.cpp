#include<iostream>
using namespace std;

bool binary_search(int a[],int high,int low,int key){
	if(low<high){
    int mid=(low+high)/2;
	if(a[mid]==key){
		return true;
	}else if(a[mid]<key){
		return binary_search(a,high,mid+1,key);
	}else{
		return binary_search(a,mid,low, key);
	}
    }
	return false;
}
void print(int a[], int n){
	if(n==0){
		return;
	}
	cout<<a[0]<<endl;
	print(a+1,n-1);
	
}

int main(){
	int a[]={1,2,3,4,5,6,7,8,9};
//	if(binary_search(a,9,0,10)){
//		cout<<"Present"<<endl;
//	}else{
//		cout<<"Absent"<<endl;
//	}
//	return 0;
    print(a,9);
}
