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

// height:- 
int maxDepth(struct Node* root) {
    if (root == NULL) {
        return 0;  // Base case: if the tree is empty, return 0
    }

    // Recursively find the depth of the left and right subtrees
    int leftDepth = maxDepth(root->left);
    int rightDepth = maxDepth(root->right);

    // The depth of the current node is 1 + max depth of the left and right subtrees
    return (leftDepth > rightDepth ? leftDepth : rightDepth) + 1;
}

//  maxxLength:-  takes O(n^2) time  
int maxlength(struct Node* root) {
    if (root == NULL) {
        return 0; 
    }

    int leftDepth = maxlength(root->left);
    int rightDepth = maxlength(root->right);
    int combo = maxDepth(root->left)+maxDepth(root->right);
    if(leftDepth>rightDepth){
    	if(leftDepth>combo) return leftDepth;
    	return combo;
	} else{
		if(rightDepth>combo) return rightDepth;
    	return combo;
	}
}

// struct for method 2:- 
struct pair{
	int dia;
	int height;
};


//maxlength Method 2: 
struct pair maxlength2(struct Node* root) {
    struct pair result;
    if (root == NULL) {
        result.dia = 0;
        result.height = 0;
        return result;
    }

    struct pair leftRes = maxlength2(root->left);
    struct pair rightRes = maxlength2(root->right);

    // Diameter calculation
    int op1 = leftRes.dia;
    int op2 = rightRes.dia;
    int op3 = leftRes.height + rightRes.height + 1;

    result.dia = (op1 > op2) ? (op1 > op3 ? op1 : op3) : (op2 > op3 ? op2 : op3);

    // Height calculation
    result.height = (leftRes.height > rightRes.height ? leftRes.height : rightRes.height) + 1;

    return result;
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
    struct pair length = maxlength2(root);
    printf("\nThe max longest path of the tree: %d\n", length.dia);
    return 0;
}

