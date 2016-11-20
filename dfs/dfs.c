/*
 *
 * Copyright - Nirlendu Saha
 * author - nirlendu@gmail.com
 *
 */

#include<stdio.h>
#include<stdlib.h>
  
struct node
{
    int key;
    struct node *left, *right;
};
  
/* Create a new node */
struct node *create_new_node(int item)
{
    struct node *temp =  (struct node *)malloc(sizeof(struct node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}
  
/* Depth First Search */
void depth_first_search(struct node *root)
{
    if (root != NULL)
    {
        depth_first_search(root->left);
        depth_first_search(root->right);
        printf("%d \n", root->key);
    }
}
  
/* Insert a new node with given key in BST */
struct node* insert_node(struct node* node, int key)
{
    /* If the tree is empty, return a new node */
    if (node == NULL) return create_new_node(key);
 
    /* Otherwise, recur down the tree */
    if (key < node->key)
        node->left  = insert_node(node->left, key);
    else if (key > node->key)
        node->right = insert_node(node->right, key);   
 
    /* return the (unchanged) node pointer */
    return node;
}
  

int main()
{
    struct node *root = NULL;
    root = insert_node(root, 50);
    insert_node(root, 30);
    insert_node(root, 20);
    insert_node(root, 40);
    insert_node(root, 70);
    insert_node(root, 60);
    insert_node(root, 80);
  
    // print DFS traversal of the BST
    printf("Printing Nodes in Depth First Search order\n");
    depth_first_search(root);
  
    return 0;
}
