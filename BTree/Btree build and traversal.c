// Build a B-tree and traversal it.

#include<stdio.h>
#include<stdlib.h>

// structur of ine node:--  
struct Btree {
	int data;
	struct Btree* right;
	struct Btree* left;
};

// size of Queue:-
int size=1;
int r=0;
int f=0;

// is Queue id Empty:-
bool isEmpty(){
	if(r==f){
		return 1;
	} else {
		return 0;
	}
}

// Queue for level order Traversal:--
int* arr=malloc(sizeOf(int));

// enQueue :-
void enQueue(int val){
	arr[++f]=val;
}

// deQueue:- 
void dequeue(){
	arr[++r]=NULL;
}


// Create Nodes :--  
struct Btree* createNode(int val){
	struct Btree * ptr= (struct Btree *)malloc(sizeof(struct Btree));
	ptr->data=val;
	ptr->left=NULL;
	ptr->right=NULL;
	return ptr;
}


// Create full tree:---  
struct Btree* createTree(){
	int val;
	printf("Enter data:");
	scanf("%d",&val);
	if(val==-1){
		return NULL;
	}
	struct Btree* root = createNode(val);
	printf("Enter data for left node of %d:\n",val);
	root->left = createTree();
	printf("Enter data for right node of %d:\n",val);
	root->right = createTree();
	
	return root;
}

// Inorder traversal:-  
void inOrder(struct Btree *root){
	if(root==NULL){
		return;
	}
	inOrder(root->left);
	printf(" %d ",root->data);
	inOrder(root->right);
};

//  level order traversal:- 

void levelOrder(struct Btree* root){
	enQueue
}


int main(){
    struct Btree* root=NULL;
    root=createTree();
    inOrder(root);
    return 0;
}
