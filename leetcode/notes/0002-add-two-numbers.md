# Add Two Numbers (Medium)

## Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](./images/0002-01.jpeg)

**Input:** l1 = [2,4,3], l2 = [5,6,4]  
**Output:** [7,0,8]  
**Explanation:** 342 + 465 = 807.

**Example 2:**

**Input:** l1 = [0], l2 = [0]  
**Output:** [0]

**Example 3:**

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]  
**Output:** [8,9,9,9,0,0,0,1]

**Constraints:**

The number of nodes in each linked list is in the range `[1, 100]`.  
$0 \leq Node.val \leq 9$  
It is guaranteed that the list represents a number that does not have leading zeros

## Solution

### Intuition

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.

![](./images/0002-02.svg)  
Figure 1. Visualization of the addition of two numbers: 342 + 465 = 807342+465=807.
Each node contains a single digit and the digits are stored in reverse order.

### Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of $l1$ and $l2$. Since each digit is in the range of $0 \ldots 90$, summing two digits may "overflow". For example $5 + 7 = 12$. In this case, we set the current digit to $2$ and bring over the $carry = 1$ to the next iteration. $carry$ must be either $0$ or $1$ because the largest possible sum of two digits (including the carry) is $9 + 9 + 1 = 19$.

The pseudocode is as following:

- Initialize current node to dummy head of the returning list.
- Initialize carry to $0$.
- Initialize $p$ and $q$ to head of $l1$ and $l2$ respectively.
- Loop through lists $l1$ and $l2$ until you reach both ends.
  - Set $x$ to node $p$'s value. If $p$ has reached the end of $l1$, set to $0$.
  - Set $y$ to node $q$'s value. If $q$ has reached the end of $l2$ set to $0$.
  - Set $sum = x + y + carry$.
  - Update $carry = sum / 10$.
  - Create a new node with the digit value of $(sum \bmod 10)$ and set it to current node's next, then advance current node to next.
  - Advance both $p$ and $q$.
- Check if $carry = 1$, if so append a new node with digit $1$ to the returning list.
- Return dummy head's next node.

Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

Take extra caution of the following cases:  
|Test Case|Explanation|
|---|---|
|l1=[0,1]<br>l2=[0,1,2]|When one list is longer than the other.|
|l1=[]<br>l2=[0,1]|When one list is null, which means an empty list.|
|l1=[9,9]<br>l2=[1]|The sum could have an extra carry of one at the end, which is easy to forget.|

### Complexity Analysis

**Time Complexity:** $O(\max(m, n))$

Assume that m and nn represents the length of l1 and l2 respectively, the algorithm above iterates at most $\max(m, n)$ times.

**Space Complexity:** $O(\max(m, n))$

The length of the new list is at most $\max(m,n) + 1$.

### Follow Up

What if the the digits in the linked list are stored in non-reversed order? For example:

$(3 \to 4 \to 2) + (4 \to 6 \to 5) = 8 \to 0 \to 7$
