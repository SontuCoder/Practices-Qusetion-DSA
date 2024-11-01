// Sum Tree :- 

#include<stdio.h>
#include<stdlib.h>

struct Node {
	struct Node* left;
	int data;
	struct Node* right;
};

struct Node* createNode(int val){
	struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
	ptr->left = NULL;
	ptr->right = NULL;
	ptr->data = val;
	return ptr;
}

struct Node* createTree(){
	int val;
	printf("Enter data:- ");
	scanf(" %d",&val);
	if(val == -1){
		return NULL;
	}
	struct Node* ptr = createNode(val);
	printf("\nEnter left of %d\n",val);
	ptr->left = createTree();
	printf("\nEnter right of %d\n",val);
	ptr->right = createTree();
	return ptr;
}

void inorder(struct Node* root){
	if(root == NULL){
		return;
	}
	inorder(root->left);
	printf(" %d ",root->data);
	inorder(root->right);
}



int main(){
	printf("Build first tree:- \n");
	struct Node* root1 = createTree();
	inorder(root1);
	
	return 0;
}






