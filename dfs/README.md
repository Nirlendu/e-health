# dfs

This is a implementation BST in C and DFS traversal

To launch, run the command

```
make
```

**Explanation**

I have used BST to explain DFS traversal. My choice of language is C because represetation of BST is intuitively better in C or C++ than other langauges.

The Wiki article says

> Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.

Essentially, in a BST, we start at `root node` and then proceed to it's children till the last level. Print the last non_visted_left_child first and then backtrack and print the last non_visited_right_child in a similar fashion. Finally backtrack and print the concerned node. It is similar in operation to `pre-order traversal` in BST. The difference being, DFS is `search` while pre-order traversal is `traversal`