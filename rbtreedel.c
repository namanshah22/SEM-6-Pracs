#include <stdio.h>
#include <stdlib.h>

// Definition of Red-Black Tree Node
typedef struct Node {
    int data;
    char color; // 'R' for Red, 'B' for Black
    struct Node *parent, *left, *right;
} Node;

// Function to create a new Red-Black Tree Node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->color = 'R'; // New node is always red
    newNode->parent = newNode->left = newNode->right = NULL;
    return newNode;
}

// Function to perform left rotation
void leftRotate(Node **root, Node *x) {
    Node *y = x->right;
    x->right = y->left;
    if (y->left != NULL)
        y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL)
        *root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;
    y->left = x;
    x->parent = y;
}

// Function to perform right rotation
void rightRotate(Node **root, Node *y) {
    Node *x = y->left;
    y->left = x->right;
    if (x->right != NULL)
        x->right->parent = y;
    x->parent = y->parent;
    if (y->parent == NULL)
        *root = x;
    else if (y == y->parent->left)
        y->parent->left = x;
    else
        y->parent->right = x;
    x->right = y;
    y->parent = x;
}

// Function to fix the Red-Black Tree violations after deletion
void fixDelete(Node **root, Node *x) {
    while (x != *root && (x == NULL || x->color == 'B')) {
        if (x == x->parent->left) {
            Node *w = x->parent->right;
            if (w->color == 'R') {
                w->color = 'B';
                x->parent->color = 'R';
                leftRotate(root, x->parent);
                w = x->parent->right;
            }
            if ((w->left == NULL || w->left->color == 'B') &&
                (w->right == NULL || w->right->color == 'B')) {
                w->color = 'R';
                x = x->parent;
            } else {
                if (w->right == NULL || w->right->color == 'B') {
                    if (w->left != NULL)
                        w->left->color = 'B';
                    w->color = 'R';
                    rightRotate(root, w);
                    w = x->parent->right;
                }
                w->color = x->parent->color;
                x->parent->color = 'B';
                if (w->right != NULL)
                    w->right->color = 'B';
                leftRotate(root, x->parent);
                x = *root;
            }
        } else {
            Node *w = x->parent->left;
            if (w->color == 'R') {
                w->color = 'B';
                x->parent->color = 'R';
                rightRotate(root, x->parent);
                w = x->parent->left;
            }
            if ((w->right == NULL || w->right->color == 'B') &&
                (w->left == NULL || w->left->color == 'B')) {
                w->color = 'R';
                x = x->parent;
            } else {
                if (w->left == NULL || w->left->color == 'B') {
                    if (w->right != NULL)
                        w->right->color = 'B';
                    w->color = 'R';
                    leftRotate(root, w);
                    w = x->parent->left;
                }
                w->color = x->parent->color;
                x->parent->color = 'B';
                if (w->left != NULL)
                    w->left->color = 'B';
                rightRotate(root, x->parent);
                x = *root;
            }
        }
    }
    if (x != NULL)
        x->color = 'B';
}

// Function to find minimum value node in a subtree
Node* minimum(Node* node) {
    while (node->left != NULL)
        node = node->left;
    return node;
}

// Function to delete a node from the Red-Black Tree
void deleteNode(Node **root, int key) {
    Node *z = *root;
    while (z != NULL) {
        if (z->data == key)
            break;
        else if (z->data < key)
            z = z->right;
        else
            z = z->left;
    }
    if (z == NULL) {
        printf("Node with key %d not found\n", key);
        return;
    }
    Node *y = z, *x;
    char yOriginalColor = y->color;
    if (z->left == NULL) {
        x = z->right;
        transplant(root, z, z->right);
    } else if (z->right == NULL) {
        x = z->left;
        transplant(root, z, z->left);
    } else {
        y = minimum(z->right);
        yOriginalColor = y->color;
        x = y->right;
        if (y->parent == z)
            x->parent = y;
        else {
            transplant(root, y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        transplant(root, z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    if (yOriginalColor == 'B')
        fixDelete(root, x);
    free(z);
}

// Function to transplant a subtree
void transplant(Node **root, Node *u, Node *v) {
    if (u->parent == NULL)
        *root = v;
    else if (u == u->parent->left)
        u->parent->left = v;
    else
        u->parent->right = v;
    if (v != NULL)
        v->parent = u->parent;
}

// Function to insert a new node into the Red-Black Tree
void insert(Node **root, int data) {
    Node *z = createNode(data);
    Node *y = NULL;
    Node *x = *root;
    while (x != NULL) {
        y = x;
        if (z->data < x->data)
            x = x->left;
        else
            x = x->right;
    }
    z->parent = y;
    if (y == NULL)
        *root = z;
    else if (z->data < y->data)
        y->left = z;
    else
        y->right = z;
    fixInsert(root, z);
}

// Function to fix the Red-Black Tree violations after insertion
void fixInsert(Node **root, Node *z) {
    while (z->parent != NULL && z->parent->color == 'R') {
        if (z->parent == z->parent->parent->left) {
            Node *y = z->parent->parent->right;
            if (y != NULL && y->color == 'R') {
                z->parent->color = 'B';
                y->color = 'B';
                z->parent->parent->color = 'R';
                z = z->parent->parent;
            } else {
                if (z == z->parent->right) {
                    z = z->parent;
                    leftRotate(root, z);
                }
                z->parent->color = 'B';
                z->parent->parent->color = 'R';
                rightRotate(root, z->parent->parent);
            }
        } else {
            Node *y = z->parent->parent->left;
            if (y != NULL && y->color == 'R') {
                z->parent->color = 'B';
                y->color = 'B';
                z->parent->parent->color = 'R';
                z = z->parent->parent;
            } else {
                if (z == z->parent->left) {
                    z = z->parent;
                    rightRotate(root, z);
                }
                z->parent->color = 'B';
                z->parent->parent->color = 'R';
                leftRotate(root, z->parent->parent);
            }
        }
    }
    (*root)->color = 'B';
}

// Function to perform in-order traversal of Red-Black Tree
void inOrderTraversal(Node *root) {
    if (root != NULL) {
        inOrderTraversal(root->left);
        printf("%d%c ", root->data, root->color);
        inOrderTraversal(root->right);
    }
}

// Function to free the memory occupied by Red-Black Tree
void freeTree(Node *root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

// Driver function
int main() {
    Node *root = NULL;
    insert(&root, 7);
    insert(&root, 3);
    insert(&root, 18);
    insert(&root, 10);
    insert(&root, 22);
    insert(&root, 8);
    insert(&root, 11);
    insert(&root, 26);
    insert(&root, 2);
    insert(&root, 6);
    insert(&root, 13);
    printf("Red-Black Tree after insertion: ");
    inOrderTraversal(root);
    printf("\n");

    deleteNode(&root, 13);
    printf("Red-Black Tree after deletion of 13: ");
    inOrderTraversal(root);
    printf("\n");

    deleteNode(&root, 18);
    printf("Red-Black Tree after deletion of 18: ");
    inOrderTraversal(root);
    printf("\n");

    freeTree(root);
    return 0;
}
