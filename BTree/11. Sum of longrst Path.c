// Sum of all nodes of the Longest Path :-

#include<stdio.h>
#include<stdlib.h>

// Structure of node
struct Node {
    struct Node* left;
    int data;
    struct Node* right;
};

// Create Node
struct Node* createNode(int val) {
    struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));
    ptr->data = val;
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

// Structure of Queue Node
struct QueueNode {
    struct Node* node;
    struct QueueNode* next;
};

// Structure of Queue
struct Queue {
    struct QueueNode* front;
    struct QueueNode* rear;
};

// Create Queue
struct Queue* createQueue() {
    struct Queue* ptr = (struct Queue*)malloc(sizeof(struct Queue));
    ptr->front = ptr->rear = NULL;
    return ptr;
}

// Check if Queue is empty
int isQueueEmpty(struct Queue* q) {
    return q->front == NULL;
}

// Enqueue
void enqueue(struct Queue* q, struct Node* node) {
    struct QueueNode* ptr = (struct QueueNode*)malloc(sizeof(struct QueueNode));
    ptr->node = node;
    ptr->next = NULL;
    if (q->front == NULL) {
        q->front = q->rear = ptr;
        return;
    }
    q->rear->next = ptr;
    q->rear = ptr;
}

// Dequeue
struct Node* dequeue(struct Queue* q) {
    if (q->front == NULL) {
        return NULL;
    }
    struct QueueNode* p = q->front;
    q->front = q->front->next;
    if (q->front == NULL) {
        q->rear = NULL;
    }
    struct Node* ptr = p->node;
    free(p);
    return ptr;
}

// Create Tree from Level order
struct Node* createTree() {
    printf("Enter data for Root: ");
    int val;
    scanf("%d", &val);
    if (val == -1) {
        return NULL;
    }

    struct Node* root = createNode(val);
    struct Queue* q = createQueue();
    enqueue(q, root);

    while (!isQueueEmpty(q)) {
        struct Node* ptr = dequeue(q);
        if (ptr == NULL) continue;

        printf("Enter data for left of %d: ", ptr->data);
        int left;
        scanf("%d", &left);
        if (left != -1) {
            struct Node* nodel = createNode(left);
            ptr->left = nodel;
            enqueue(q, nodel);
        }

        printf("Enter data for right of %d: ", ptr->data);
        int right;
        scanf("%d", &right);
        if (right != -1) {
            struct Node* noder = createNode(right);
            ptr->right = noder;
            enqueue(q, noder);
        }
    }
    return root;
}

// struct Of every node of (height, sum):- 
 struct pair{
 	int height;
 	int sum;
 };

// Max depth or height of tree
struct pair* maxDepth(struct Node* root) {
	struct pair* ptr = (struct pair*)malloc(sizeof(struct pair));
    if (root == NULL) { // base case
        ptr->height=0; 
		ptr->sum = 0;
		return ptr; 
    }

    // Recursively find the depth of the left and right subtrees
    struct pair* left = maxDepth(root->left);
    struct pair* right = maxDepth(root->right);
    
    if(left->height == right->height){
    	ptr->sum = (left->sum > right->sum ? left->sum : right->sum) + root->data;
		ptr->height = left->height+1;
	} else if(left->height > right->height){
		ptr->sum = left->sum + root->data;
		ptr->height = left->height+1;
	} else{
		ptr->sum = right->sum + root->data;
		ptr->height = right->height+1;
	}
	free(left);
	free(right);
    return ptr;
}


// Inorder Traversal
void inorder(struct Node* root) {
    if (root == NULL) {
        return;
    }
    inorder(root->left);
    printf(" %d ", root->data);
    inorder(root->right);
}

int main() {
    struct Node* root = createTree();
    printf("\nInorder Traversal: ");
    inorder(root);

    // Calculate the maximum depth of the tree
    struct pair* depth = maxDepth(root);
    printf("\nThe depth or height of the tree: %d, %d\n", depth->sum,depth->height);
    return 0;
}

