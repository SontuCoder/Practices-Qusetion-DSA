// Balanced Tree  

#include<stdio.h>
#include<stdlib.h>

struct Node{
	int data;
	struct Node* right;
	struct Node* left;
};

struct Node* createNode(int val){
	struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
	ptr->data = val;
	ptr->left = NULL;
	ptr->right = NULL;
	return ptr;
}

struct Node* createTree(){
	int val;
	printf("Enter data:- ");
	scanf("%d",&val);
	if(val == -1){
		return NULL;
	} else {
		struct Node* ptr = createNode(val);
		
		printf("Enter data in left of %d:-\n",ptr->data);
		ptr->left = createTree();
		
		printf("Enter data in right of %d:-\n",ptr->data);
		ptr->right = createTree();
		
		return ptr;
	}
}

void inorder(struct Node* root){
	if(root==NULL){
		return;
	}
	inorder(root->left);
	printf(" %d ",root->data);
	inorder(root->right);
}

int height(struct Node* root){
	if(root == NULL){
		return 0;
	}
	return (height(root->left)>height(root->right) ? height(root->left) : height(root->right)) +1;
}

// Method 1 : Takes O(n^2)  
int balanced(struct Node* root){
	if(root == NULL){
		return 1;
	} 
	
	int left_balance = balanced(root->left);
	int right_balance = balanced(root->right);
	if(left_balance == 0 || right_balance == 0) return 0;
	if(abs(height(root->left)-height(root->right))<=1){
		return 1;
	} else {
		return 0;
	}
}


// Method 2 : Takes O(n) 
struct Pair{
	int balanced;
	int height;
};

struct Pair balanced2(struct Node* root){
	struct Pair ptr;
	if(root == NULL){
		ptr.balanced = 1;
		ptr.height = 0;
		return ptr;
	}
	
	struct Pair left = balanced2(root->left);
	struct Pair right = balanced2(root->right);
	
	if(left.balanced == 0 || right.balanced == 0 || (abs(left.height - right.height)>1)){ 
		ptr.balanced = 0;
	} else {
		ptr.balanced = 1;
	}
	
	ptr.height = ((left.height<right.height) ? right.height : left.height)+1;
	return ptr;
}

int main(){
	printf("Create Tree:-\n");
	struct Node* root = createTree();
	inorder(root);
	if(balanced2(root).balanced){
		printf("\nBalanced");
	} else {
		printf("\nNot Balanced");
	}
	return 0;
}
