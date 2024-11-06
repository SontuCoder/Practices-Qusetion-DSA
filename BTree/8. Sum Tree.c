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

struct sumNode {
	int isSum;
	int total;
};

struct sumNode* checkSum(struct Node* root){
	struct sumNode* ptr =(struct sumNode*)malloc(sizeof(struct sumNode));
	if(root==NULL){
		ptr->isSum = 1;
		ptr->total = 0;
		return ptr;
	}
	if(root->left == NULL && root->right == NULL){
	 	ptr->isSum = 1;
		ptr->total = root->data;
		return ptr;
	}
	struct sumNode* left = checkSum(root->left);
	struct sumNode* right = checkSum(root->right);
	
	if(left->isSum == 0 || right->isSum == 0 || (root->data != left->total + right->total)){
		ptr->isSum = 0;
	} else {
		ptr->isSum = 1;
	}
	
	ptr->total = root->data + left->total + right->total;
	return ptr;
}

int main(){
	printf("Build first tree:- \n");
	struct Node* root1 = createTree();
	inorder(root1);
	struct sumNode* result = checkSum(root1);
	if(result->isSum){
		printf("\nYes");
	} else {
		printf("\nNo..!");
	}
	return 0;
}






