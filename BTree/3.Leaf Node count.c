// Count Leaf Nodes:- 

#include<stdio.h>
#include<stdlib.h>

// structur of node:--
 struct Node{
   	struct Node* left;
 	int data;
 	struct Node* right;
 };
 
// crate Node:--
 struct Node* createNode(int val){
 	struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
 	ptr->data= val;
 	ptr->left = NULL;
 	ptr->right = NULL;
 	return ptr;
 }
 
 
// struct of Queue Node:-

struct QueueNode{
	struct Node* node;
	struct QueueNode* next;
};

// struct of Queue:-- 

struct Queue{
	struct QueueNode* front;
	struct QueueNode* rear;
};

// create Queue:-- 
struct Queue* createQueue(){
	struct Queue* ptr= (struct Queue*)malloc(sizeof(struct Queue));
	ptr->front=ptr->rear=NULL;
	return ptr;
}

// enqueue:- 
void enqueue(struct Queue* q, struct Node* node){
	struct QueueNode* ptr = (struct QueueNode*)malloc(sizeof(struct QueueNode));
	ptr->node=node;
	ptr->next=NULL;
	if(q->rear==NULL){
		q->front=q->rear=ptr;
		return;
	}
	q->rear->next=ptr;
	q->rear=ptr;
}

// dequeue:- 
struct Node* dequeue(struct Queue* q){
	if(q->front==NULL){
		return NULL;
	}
	struct QueueNode* ptr = q->front;
	q->front=q->front->next;
	
	if(q->front==NULL){
		q->rear=NULL;
	}
	struct Node* tempNode = ptr->node;
	free(ptr);
	return tempNode;
}

// check if Queue is Null or Not:- 

int isQueueEmpty(struct Queue* q){
	return q->front==NULL;
}

// Create Tree from Level order travers:- 
struct Node* createTreeLevel(){
	struct Queue* q = createQueue();
	printf("Enter tha data from root:- ");
	int val;
	scanf("%d",&val);
	if(val==-1) return NULL;
	struct Node* root=createNode(val);
	enqueue(q,root);
	
	while(!isQueueEmpty(q)){
		struct Node* node = dequeue(q);
		// left Node:-  
		printf("Enter tha data from left of %d:- ",node->data);	    
		int left;
	    scanf("%d",&left);
	    if(left!=-1){
	    	node->left=createNode(left);
	        enqueue(q,node->left);
		}
	    
	    // right Node:-  
		printf("Enter tha data from right of %d:- ",node->data);
	    int right;
	    scanf("%d",&right);
	    if(right!=-1){
	    	node->right=createNode(right);
	        enqueue(q,node->right);
		}
	}
	return root;
}

// Method 1 :- 
int countLeaf(struct Node* root){
	if(root->left==NULL && root->right==NULL){
		return 1;
	} else if(root->left==NULL && root->right!=NULL){
		return countLeaf(root->right);
	} else if(root->left!=NULL && root->right==NULL){
		return countLeaf(root->left);
	} else {
		return countLeaf(root->left)+countLeaf(root->right);
	}
}

// Count leaf node by Inorder travers :- 
void countInorder(struct Node* root,int* count){
	if(root==NULL) return ;
	countInorder(root->left,count);
	if(root->left==NULL && root->right==NULL){
		(*count)++;
	}
	countInorder(root->right,count);
}


int main(){
	printf("Build tree from Levelorder:- \n");
	struct Node* root = createTreeLevel();
	printf("\n");
	printf("The Count Leaf node by travers:- \n");
	printf("Number of Leaf Node is:- %d\n",countLeaf(root));
	int count=0;
	printf("The Count Leaf node by Inorder travers:- \n");
	countInorder(root,&count);
	printf("Number of Leaf Node is:- %d\n",count);
	return 0;	
	
}





