/*
 * Depth First Binary Tree Search using Recursion
 * Nirlendu Saha, 2016
 */
#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int data;
    struct node *left;
    struct node *right;
};
 
void build_node(struct node **, int);
void depth_first_traversal(struct node *);
void delete_tree(struct node **);
 
int main()
{
    struct node *head = NULL;
    int choice = 0, num, flag = 0, key;
 
    // do
    // {
    //     printf("\nEnter your choice:\n1. Insert\n2. Perform DFS Traversal\n3. Exit\nChoice: ");
    //     scanf("%d", &choice);
    //     switch(choice)
    //     {
    //     case 1: 
    //         printf("Enter element to insert: ");
    //         scanf("%d", &num);
    //         build_node(&head, num);
    //         break;
    //     case 2: 
    //         depth_first_traversal(head);
    //         break;
    //     case 3: 
    //         delete_tree(&head);
    //         printf("Memory Cleared\nPROGRAM TERMINATED\n");
    //         break;
    //     default: 
    //         printf("Not a valid input, try again\n");
    //     }
    // } while (choice != 3);

    return 0;
}
 
void build_node(struct node **head, int data)
{
    struct node *temp = *head, *prev = *head;
 
    if (*head == NULL)
    {
        *head = (struct node *)malloc(sizeof(struct node));
        (*head)->data = data;
        (*head)->left = (*head)->right = NULL;
    }
    else
    {
        while (temp != NULL)
        {
            if (data > temp->data)
            {
                prev = temp;
                temp = temp->right;
            }
            else
            {
                prev = temp;
                temp = temp->left;
            }
        }
        temp = (struct node *)malloc(sizeof(struct node));
        temp->data = data;
        if (data >= prev->data)
        {
            prev->right = temp;
        }
        else
        {
            prev->left = temp;
        }
    }
}
 
void depth_first_traversal(struct node *head)
{
    if (head)
    {
        if (head->left)
        {
            depth_first_traversal(head->left);
        }
        if (head->right)
        {
            depth_first_traversal(head->right);
        }
        printf("%d  ", head->data);
    }
}
 
void delete_tree(struct node **head)
{
    if (*head != NULL)
    {
        if ((*head)->left)
        {
            delete_tree(&(*head)->left);
        }
        if ((*head)->right)
        {
            delete_tree(&(*head)->right);
        }
        free(*head);
    }
}