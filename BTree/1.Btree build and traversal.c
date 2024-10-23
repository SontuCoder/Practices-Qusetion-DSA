#include<stdio.h>
#include<stdlib.h>

// Structure of one node
struct Btree {
    int data;
    struct Btree* right;
    struct Btree* left;
};

// Create Nodes
struct Btree* createNode(int val) {
    struct Btree* ptr = (struct Btree*)malloc(sizeof(struct Btree));
    ptr->data = val;
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

// Structure for a queue node
struct QueueNode {
    struct Btree* treeNode;
    struct QueueNode* next;
};

// Queue structure
struct Queue {
    struct QueueNode* front;
    struct QueueNode* rear;
};

// Function to create an empty queue
struct Queue* createQueue() {
    struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}

// Function to enqueue a tree node
void enqueue(struct Queue* q, struct Btree* treeNode) {
    struct QueueNode* temp = (struct QueueNode*)malloc(sizeof(struct QueueNode));
    temp->treeNode = treeNode;
    temp->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
}

// Function to dequeue a tree node
struct Btree* dequeue(struct Queue* q) {
    if (q->front == NULL) {
        return NULL;
    }
    struct QueueNode* temp = q->front;
    q->front = q->front->next;

    if (q->front == NULL) {
        q->rear = NULL;
    }

    struct Btree* treeNode = temp->treeNode;
    free(temp);
    return treeNode;
}

// Function to check if the queue is empty
int isQueueEmpty(struct Queue* q) {
    return q->front == NULL;
}

// Create full tree
struct Btree* createTree() {
    int val;
    printf("Enter data: ");
    scanf("%d", &val);
    if (val == -1) {
        return NULL;
    }
    struct Btree* root = createNode(val);
    printf("Enter data for left node of %d:\n", val);
    root->left = createTree();
    printf("Enter data for right node of %d:\n", val);
    root->right = createTree();

    return root;
}

// Inorder traversal
void inOrder(struct Btree* root) {
    if (root == NULL) {
        return;
    }
    inOrder(root->left);
    printf(" %d ", root->data);
    inOrder(root->right);
}

// Function for level order traversal using a queue, printing each level on a new line
void levelOrderTraversal(struct Btree* root) {
    if (root == NULL) {
        return;
    }

    struct Queue* q = createQueue();
    enqueue(q, root);
    enqueue(q, NULL);  // Delimiter for the end of a level

    while (!isQueueEmpty(q)) {
        struct Btree* currentNode = dequeue(q);

        if (currentNode == NULL) {
            // End of current level
            printf("\n");

            // If there are more nodes to process, add a new delimiter for the next level
            if (!isQueueEmpty(q)) {
                enqueue(q, NULL);
            }
        } else {
            printf("%d ", currentNode->data);

            if (currentNode->left != NULL) {
                enqueue(q, currentNode->left);
            }

            if (currentNode->right != NULL) {
                enqueue(q, currentNode->right);
            }
        }
    }
}

int main() {
    struct Btree* root = NULL;
    root = createTree();
    printf("Level Order Traversal: \n");
    levelOrderTraversal(root);
    return 0;
}

