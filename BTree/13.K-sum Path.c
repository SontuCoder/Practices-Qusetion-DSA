#include <stdio.h>
#include <stdlib.h>

// Define max path size and initialize path array
#define MAX_SIZE 50

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

// Inorder Traversal
void inorder(struct Node* root) {
    if (root == NULL) {
        return;
    }
    inorder(root->left);
    printf(" %d ", root->data);
    inorder(root->right);
}

// k-sum path using array-based path storage
void countPath(struct Node* root, int k, int* path, int pathLen, int* count) {
    if (root == NULL) return;

    // Store current node in path
    path[pathLen++] = root->data;

    // Recursive calls for left and right subtrees
    countPath(root->left, k, path, pathLen, count);
    countPath(root->right, k, path, pathLen, count);

    // Check paths that sum up to k
    int sum = 0;
    int i;
    for (i = pathLen - 1; i >= 0; i--) {
        sum += path[i];
        if (sum == k) {
            (*count)++;
        }
    }
}

int numPath(struct Node* root, int k) {
    int path[MAX_SIZE];
    int count = 0;
    countPath(root, k, path, 0, &count);
    return count;
}

int main() {
    struct Node* root = createTree();
    printf("\nInorder Traversal: ");
    inorder(root);
    int k;
    printf("\nEnter the path sum: ");
    scanf("%d", &k);
    printf("\nNumber of Paths: %d", numPath(root, k));
    return 0;
}

