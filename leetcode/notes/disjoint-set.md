# Disjoint Set

## Introduction

Given the vertices and edges between them, how could we quickly check whether two vertices are connected? For example, Figure 5 shows the edges between vertices, so how could we quickly check, respectively, if (0, 3), (1, 5), and (7, 8) are connected? We can figure this out using the “disjoint set” data structure, also known as the “union-find” data structure. Others might refer to it as an algorithm. In this Explore Card, the term “disjoint set” refers to a data structure.

[figure 5](./assets/disjoint-set-01.png)
Figure 5. The connectivity question

The primary use of disjoint sets is to address the connectivity between the components of a network. The “network” here can be a computer network or a social network. For instance, we can use a disjoint set to determine if two people share a common ancestor.

### Terminologies

**Parent node**: the direct parent node of a vertex. For example, in Figure 5, the parent node of vertex 3 is 1, the parent node of vertex 2 is 0, and the parent node of vertex 9 is 9.  
**Root node**: a node without a parent node, and it can be viewed as its own parent node. For example, in Figure 5, the root nodes of vertices 3 and 2 are both 0. 0 is its own parent node and its own root node. The root node of vertex 9 is 9 itself.

### The two important functions of a “disjoint set.”

In the introduction videos above, we discussed the two important functions in a “disjoint set”.

- **The _find_ function** finds the root node of a given vertex. For example, in Figure 5, the output of the find function for vertex 3 is 0.
- **The _union_ function** unions two vertices and makes their root nodes the same. In Figure 5, if we union vertex 4 and vertex 5, their root node will become the same, which means the union function will modify the root node of vertex 4 or vertex 5 to the same root node.

### There are two ways to implement a “disjoint set”.
- Implementation with Quick Find: in this case, the time complexity of the **find** function will be O(1). However, the **union** function will take more responsibility with the time complexity of O(N).
- Implementation with Quick Union: compared with the Quick Find implementation, the time complexity of the **union** function is better. Meanwhile, the **find** function takes more responsibility.

## Quick Find

### Implementation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
```

### Time Complexity

|                 | Union-find<br>Constructor | Find | Union | Connected |
|-----------------|:-------------------------:|:----:|:-----:|:---------:|
| Time complexity |           O(N)            | O(1) |  O(N) |   O(1)    |

_Note_: N is the number of vertices in the graph.

## Union Find

### Implmentation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
```

### Time Complexity

|                 | Union-find<br>Constructor | Find | Union | Connected |
|-----------------|:-------------------------:|:----:|:-----:|:---------:|
| Time complexity |           O(N)            | O(H) |  O(H) |   O(H)    |

_Note_: N is the number of vertices in the graph. H is the height of the tree.

## Union by Rank

We have implemented two kinds of “disjoint sets” so far, and they both have a concerning disadvantage. Specifically, all the vertices may form a line after connecting vertices using union, as shown in Figure 5, which is the worst-case scenario for the find function. Is there any way to optimize it?

Of course, there is; it is to union by rank. The word “rank” means ordering by specific criteria. Previously, for the union function, we randomly choose a root node/parent node of x or y and set it as the new root node for the other vertex. However, to union by rank, we must choose the parent node based on certain criteria.

To be specific, the “rank” refers to the height of each vertex. When we union two vertices, instead of randomly picking one of the root nodes as the new root node, we choose the root node of the vertex with a larger “rank”. We will merge the shorter tree under the taller tree and assign the root node of the taller tree as the root node for both vertices. In this way, we effectively avoid the possibility of connecting all vertices into a straight line. This optimization is called the “disjoint set” with union by rank.

[figure 5](./assets/disjoint-set-union-by-rank.png)

### Implementation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5--7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true6
```

### Time Complexity

|                 | Union-find<br>Constructor |  Find   |  Union   | Connected |
|-----------------|:-------------------------:|:-------:|:--------:|:---------:|
| Time complexity |           O(N)            | O(logN) |  O(logN) |   O(logN) |

_Note_: N is the number of vertices in the graph.

## Path Compression Optimization

In the previous implementation of the “disjoint set”, we notice that we need to traverse the parent nodes sequentially until we reach the root node to find the root node. If we search the root node of the same element again, we repeat the same operations. Is there any way to optimize it?

The answer is yes! After finding the root node, we can update the parent node of all traversed elements to their root node. When we search for the root node of the same element again, we only need to traverse two elements to find its root node, which is highly efficient. So, how could we efficiently update the parent nodes of all traversed elements to the root node? The answer is to use “recursion”. This optimization is called “path compression”, which optimizes the **find** function.

### Implementation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
```

### Time Complexity

|                 | Union-find<br>Constructor |  Find   |  Union   | Connected |
|-----------------|:-------------------------:|:-------:|:--------:|:---------:|
| Time complexity |           O(N)            | O(logN) |  O(logN) |   O(logN) |

_Note_: N is the number of vertices in the graph.

## Optimized “disjoint set” with Path Compression and Union by Rank

This implementation of the “disjoint set” is optimized with both “path compression” and “union by rank”.

### Implementation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
```

### Time Complexity

|                 | Union-find<br>Constructor |  Find | Union  | Connected |
|-----------------|:-------------------------:|:-----:|:------:|:---------:|
| Time complexity |           O(N)            | O(⍺N) |  O(⍺N) |   O(⍺N)   |

_Note_: N is the number of vertices in the graph. ⍺ refers to the Inverse Ackermann function. In practice, we assume it's a constant. In other words, O(⍺(N)) is regarded as O(1) on average. 

## Summary

The main idea of a “disjoint set” is to have all connected vertices have the same parent node or root node, whether directly or indirectly connected. To check if two vertices are connected, we only need to check if they have the same root node.

The two most important functions for the “disjoint set” data structure are the **find** function and the **union** function. The **find** function locates the root node of a given vertex. The **union** function connects two previously unconnected vertices by equating their root node. There is another important function named **connected**, which checks the “connectivity” of two vertices. The **find** and **union** functions are essential for any question requiring the “disjoint set” data structure, while only some of the questions need the **connected** function.

### Implementation

#### Basic Disjoint Set

```python
class UnionFind:
    # Constructor of Union-find. The size is the length of the root array.
    def __init__(self, size):
    def find(self, x):
    def union(self, x, y):
    def connected(self, x, y):
```

#### Find Function

```python
def find(self, x):
    while x != self.root[x]:
        x = self.root[x]
    return x
```

#### Find Function - Optmized With Path Compression

```python
def find(self, x):
    if x == self.root[x]:
        return x
    self.root[x] = self.find(self.root[x])
    return self.root[x]
```

#### Union Function

```python
def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
        self.root[rootY] = rootX
```

#### Union Function - Optimized By Union Rank

```python
def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
```

#### Connected Function

The connected function checks if two vertices, x and y, are connected by checking if they have the same root node. If x and y have the same root node, they are connected. Otherwise, they are not connected.

```python
def connected(self, x, y):
    return self.find(x) == self.find(y)
```

### Tips for using the “disjoint sets” data structure in solving LeetCode problems

The code for the disjoint set is highly modularized. You might want to get familiar with the implementation. I would highly recommend that you understand and memorize the implementation of“disjoint set with path compression and union by rank”.

Finally, please try to solve the exercise problems using the abovementioned implementation of the “disjoint set” data structure. These problems might be solved using other algorithms and data structures, but I would highly recommend you to solve them using the “disjoint set” data structure.
