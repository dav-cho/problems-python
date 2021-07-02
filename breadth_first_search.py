class Node:
    def __init__(self, value) -> None:
        self.left: Node = None
        self.right: Node = None
        self.value = value
        # self.left = None
        # self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node = None
        # self.root = None

    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node

        else:
            current_node = self.root

            while True:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left

                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

        return self

    def lookup(self, value):
        if not self.root:
            return None

        current_node = self.root

        while current_node:
            if value < current_node.value:
                current_node = current_node.left

            elif value > current_node.value:
                current_node = current_node.right

            elif value is current_node.value:
                return current_node

        return None

    def remove(self, value):
        if not self.root:
            return None

        parent_node = None
        current_node = self.root

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            elif value is current_node.value:
                if not current_node.right:
                    if not parent_node:
                        self.root = current_node.left

                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left

                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left

                elif not current_node.right.left:
                    current_node.right.left = current_node.left

                    if not parent_node:
                        self.root = current_node.right

                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right

                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right

                else:
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right

                    while leftmost.left:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if not parent_node:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost

                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost

                return True

    def breadth_first_search(self):
        current_node: Node = self.root
        list = []
        queue = []

        queue.append(current_node)

        while len(queue):
            current_node = queue.pop(0)
            list.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return list


my_BST = BinarySearchTree()
my_BST.insert(9)
my_BST.insert(4)
my_BST.insert(6)
my_BST.insert(20)
my_BST.insert(170)
my_BST.insert(15)
my_BST.insert(1)
my_BST_lookup1 = my_BST.lookup(15)
print("~ BST lookup 1", my_BST_lookup1.value)
my_BST_lookup2 = my_BST.lookup(7)
print("~ BST lookup 2", my_BST_lookup2.value) if my_BST_lookup2 else None
# print(my_BST.root.value)

my_BST_BFS = my_BST.breadth_first_search()
print(my_BST_BFS)

my_BST.insert(27)
# my_BST.insert(33)
# my_BST.insert(2)
my_BST_BFS2 = my_BST.breadth_first_search()
print(my_BST_BFS2)

# my_BST.remove(27)
# my_BST.remove(33)
# my_BST.remove(2)
# my_BST_BFS3 = my_BST.breadth_first_search()
# print(my_BST_BFS3)

#           9
#       4      20
#     1   6  15  170
#
#               9
#         4           20
#      2     6    15      27
#   1                   33  170

#           9
#       4      20
#     1   6  15  170
#       2       27
#                 33
#
#   if value < current_node.value:
#             if not current_node.left:
#                 current_node.left = new_node
#                 return self
#             current_node = current_node.left

#         else:
#             if not current_node.right:
#                 current_node.right = new_node
#                 return self
#             current_node = current_node.righ
