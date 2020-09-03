# Greedy Approach

## Definition:

- Greedy Algorithm is a paradigm that builds up a solution piece by piece, always choosing the piece that offers 
the most obvious and immediate benefit. So the problem where choosing locally optimal also leads to global solutions are the best fit for Greedy

- Greedy are best used for optimization problems. An optimization problem can be solved using Greedy if the problem is: 
At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem. 

- This is more optimal than Dynamic Programming, but it cannot be used in every problem. 


## Types of problem: 

1.  Kruskal's Minimum Spanning Tree:

+ What is a minimum spanning tree? 
        - Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together 
        - A minimum spanning tree (MST) for a weighted, connected and undirected graph os a spanning tree with weight less than or equals to the weight of every other spanning tree . 
        - The weight of a spanning tree is the sum of weights given to each edge of the spanning tree. 
+ Algorithm:
```
1. Sort all of the edges in non-decreasing order of their weight
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge, Else, discrad it. 
3. Repeat #2 until there are (V-1) edges in the spanning tree. 

```
+ The algorithm is a Greedy Algorithm. The greedy choice is to pick the smallest weight edge that does not cause a cycle in the MST constructed so far. 
    
2.  Prim's Minimum Spanning Tree

3.  Dikstra's shortest path

4.  Huffman Coding

5. Activity selection problem



## When To Use Greedy Algorithm?

- We use the greedy algorithm when the problem sastisfies these two properties: 
    + Greedy - choice property: A global optimum can be arrived at by selecting a local optimum
    + Optimal substructure: An optimal solutions to the problem can contains an optimal solution to the problems



## Example codes: 

- Activity Selection Problem:
    + The problem is to select the maximum number of activities that can be performed by a single person or machine, assuming that a person can only work on a single activity at a time
    + Source code: activitySelction.py

- Egyptian Fraction: 
    + 
    + Source code: Egyptian Fraction
