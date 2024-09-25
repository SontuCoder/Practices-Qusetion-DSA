#include<stdio.h>
void print(char a[],int n){
	if(n==0){
		return;
	}
	printf("%c",a[0]);
	print(a+1,n-1);
}

void swap(char a[],int j,int n){
	char b=a[j];
		a[j]=a[n];
		a[n]=b;
}

void permutation(char a[],int n,int i){
	if(i==n){
		return;
	}
	
	int j;
	for(j=i;j<n;j++){
		swap(a,j,i);
	    print(a,n);
	    printf("\n");
	    swap(a,j,i);
	}
//	permutation(a,n,i+1);
	
}


int main(){
	char a[]="abc";
	permutation(a,3,0);
//    print(a,3);
//    printf("%s",a);
}
