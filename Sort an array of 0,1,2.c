// sort a array which contains either 0s, 1s, or 2s:
// [0,1,2,1,1,0] => [0,0,1,1,1,2]                   


#include<stdio.h>

void marge(int arr[], int low, int mid, int high){
	int i=low,k=low, j=mid+1;
	int a[high+1];
	while(i<mid+1 && j<high+1){
		if(arr[i]<arr[j]){
			a[k++]=arr[i++];
		}
		else{
			a[k++]=arr[j++];
		}
	}
	while(i<mid+1){
		a[k++]=arr[i++];
	}
	while(j<high+1){
		a[k++]=arr[j++];
	}
	for(i=low; i<high+1; i++){
		arr[i]=a[i];
	}
}


void sort(int arr[],int low, int high){
	if(low<high){
		int mid = (low+high)/2;
		sort(arr, low,mid);
		sort(arr, mid+1, high);
		marge(arr, low, mid, high);
	}
}


void main(){
	int n;
	printf("Enter the number of element: ");
	scanf("%d",&n);
	int arr[n];
	int i;
	for(i=0; i<n; i++){
		printf("Enter element: ");
		scanf("%d",&arr[i]);
	}
	printf("The array Befor sorted: ");
	for(i=0; i<n; i++){
		printf("%d ",arr[i]);
	}
	printf("\n");
	sort(arr,0,n-1);
	printf("Array after sorted: ");
	for(i=0; i<n; i++){
		printf("%d ",arr[i]);
	}
}
