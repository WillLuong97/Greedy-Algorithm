# Greedy Approach

## Definition:

- Greedy Algorithm is a paradigm that builds up a solution piece by piece, always choosing the piece that offers 
the most obvious and immediate benefit. So the problem where choosing locally optimal also leads to global solutions are the best fit for Greedy

- Greedy are best used for optimization problems. An optimization problem can be solved using Greedy if the problem is: 
At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem. 

- This is more optimal than Dynamic Programming, but it cannot be used in every problem. 


## Types of problem: 

1/ Kruskal's Minimum Spanning Tree: we create a MST by picking the edges one by one. The Greedy choice is pick the smallest weight edge that doesn't cause a cycle in the MST constructed so far. 

2/ Prim's Minimum Spanning Tree

3/ Dikstra's shortest path

4/ Huffman Coding

5/ Activity selection problem



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
