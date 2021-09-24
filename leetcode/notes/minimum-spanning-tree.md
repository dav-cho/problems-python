# Minimum Spanning Tree

You might wonder: what is a spanning tree? A **spanning tree** is a connected subgraph in an undirected graph where **all vertices** are connected with the **minimum number** of edges. In Figure 8, all pink edges [(A, B), (A, C), (A, D), (A, E)] form a tree, which is a spanning tree of this undirected graph. Note that [(A, E), (A, B), (B, C), (C, D)] is also a spanning tree of the undirected graph. Thus, an “undirected graph” can have multiple spanning trees.

[Figure 8. Spanning tree](./assets/min-spanning-tree-01.png)  
Figure 8. Spanning Tree

After knowing what a spanning tree is, you might have raised another question: what is a **minimum spanning tree**? A minimum spanning tree is a spanning tree with the minimum possible total edge weight in a “weighted undirected graph”. In Figure 9, a spanning tree formed by green edges [(A, E), (A, B), (B, C), (C, D)] is one of the minimum spanning trees in this weighted undirected graph. Actually, [(A, E), (E, D), (A, B), (B, C)] forms another minimum spanning tree of the weighted undirected graph. Thus, a “weighted undirected graph” can have multiple minimum spanning trees.

[Figure 9. Minimum Spanning tree](./assets/min-spanning-tree-02.png)  
Figure 9. Spanning Tree

In this chapter, we will learn two algorithms for constructing a “minimum spanning tree”, and the “cut property”:

- Cut Property
- Kruskal’s Algorithm
- Prim’s algorithm

## Cut Property

What is a “cut”? Although many theorems are named after people’s names, “cut” is not one of them. To understand the “Cut property”, we need to understand two basic concepts.

- First, in Graph theory, a “cut” is a partition of vertices in a “graph” into two disjoint subsets. Figure 10 illustrates a “cut”, where (B, A, E) forms one subset, and (C, D) forms the other subset.
- Second, a crossing edge is an edge that connects a vertex in one set with a vertex in the other set. In Figure 10, (B, C), (A, C), (A, D), (E, D) are all “crossing edges”.

[Figure 10. Graph with a cut](./assets/min-spanning-tree-03.png)  
Figure 10. Graph with a cut

After knowing the basics of a graph cut, let’s delve into the “Cut property”. The Cut property provides theoretical support for Kruskal’s algorithm and Prim’s algorithm. So, what is the “Cut property”? According to [Wikipedia](https://en.wikipedia.org/wiki/Minimum_spanning_tree#Cut_property), the “Cut property” refers to:

> For any cut C of the graph, if the weight of an edge e in the cut-set of C is strictly smaller than the weights of all other edges of the cut-set of C, then this edge belongs to all MSTs of the graph.

## Kruskal's Algorithm

“Kruskal’s algorithm” is an algorithm to construct a “minimum spanning tree” of a “weighted undirected graph”.

### Steps

1. Ascending sort all edges by their weight.
2. Add edges in that order into the Minimum Spanning Tree. Skip the edges that would produce cycles in the MST.
3. Repeat step 2 until N - 1 edges are added.

### Time Complexity

Time: O(E logE) - E represents the number of edges.
Space: O(V) - V represents the number of vertices.

## Prim's Algorithm

“Prim’s algorithm” is another algorithm for constructing a “minimum spanning tree” of a “weighted undirected graph”.

### The difference between the “Kruskal’s algorithm” and the “Prim’s algorithm”:

“Kruskal’s algorithm” expands the “minimum spanning tree” by adding edges. Whereas “Prim’s algorithm” expands the “minimum spanning tree” by adding vertices.

### Time Complexity

Binary heap: O(ElogV)  
Fibonacci heap: O(E+VlogV)

V represents the number of vertices, and E represents the number of edges.

### Space Complexity

O(V)

V represents the number of vertices.

