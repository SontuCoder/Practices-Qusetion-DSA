// Identical Tree :- 

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

int identical(struct Node* root1, struct Node* root2) {
    if (root1 == NULL && root2 == NULL) return 1;
    if (root1 == NULL || root2 == NULL) return 0;

    return (root1->data == root2->data) && identical(root1->left, root2->left) && identical(root1->right, root2->right);
}

int main(){
	printf("Build first tree:- \n");
	struct Node* root1 = createTree();
	printf("Build second tree:- \n");
	struct Node* root2 = createTree();
	inorder(root1);
	printf("\n");
	inorder(root2);
	if(identical(root1, root2)){
		printf("\n Yes! ");
	} else {
		printf("\n No! ");
	}
	return 0;
}






