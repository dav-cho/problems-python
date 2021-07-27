##
#### Design Linked List (medium)
####################################

# Design your implementation of the linked list. You can choose to use
# a singly or doubly linked list.

# A node in a singly linked list should have two attributes: val and next.
# val is the value of the current node, and next is a pointer/reference
# to the next node.

# If you want to use the doubly linked list, you will need one more
# attribute prev to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:
# - MyLinkedList() Initializes the MyLinkedList object.
# - int get(int index) Get the value of the indexth node in the linked list.
#   If the index is invalid, return -1.
# - void addAtHead(int val) Add a node of value val before the first element
#   of the linked list. After the insertion, the new node will be the
#   first node of the linked list.
# - void addAtTail(int val) Append a node of value val as the last element
#   of the linked list.
# - void addAtIndex(int index, int val) Add a node of value val before the
#   indexth node in the linked list. If index equals the length of the
#   linked list, the node will be appended to the end of the linked
#   list. If index is greater than the length, the node will not be inserted.
# - void deleteAtIndex(int index) Delete the indexth node in the linked list,
#   if the index is valid.

# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

# Constraints:
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex
# and deleteAtIndex.

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

################################################################################


## singly linked list
#########################
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next

        return curr.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        new = ListNode(val)
        new.next = prev.next
        prev.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1


## doubly linked list
#########################
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return - 1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.tail
        new.prev = self.tail.prev
        self.tail.prev.next = new
        self.tail.prev = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next
        else:
            next = self.tail
            for _ in range(self.size - index):
                next = next.prev
            prev = next.prev

        new = ListNode(val)
        new.next = next
        new.prev = prev
        prev.next = new
        next.prev = new
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next.next
        else:
            next = self.tail
            for _ in range(self.size - index - 1):
                next = next.prev
            prev = next.prev.prev

        prev.next = next
        next.prev = prev
        self.size -= 1

        
## Tests
############

test1 = MyLinkedList()
test1.addAtHead(1)
print(test1.get(0))
test1.addAtTail(3)
print(test1.get(1))
test1.addAtIndex(1, 2)    # linked list becomes 1 -> 2 -> 3
print(test1.get(0), test1.get(1), test1.get(2))
print(test1.get(1))              # return 2
test1.deleteAtIndex(1);    # now the linked list is 1 -> 3
print(test1.get(0), test1.get(1))
print(test1.get(1))              # return 3

#test2 = MyLinkedList()
#test2.addAtHead(1)
#print(test2.get(0))
#test2.deleteAtIndex(0)

#test3 = MyLinkedList()
#test3.addAtHead(7)
#print(test3.head.val)
#test3.addAtHead(2)
#print(test3.head.val, test3.get(1))
#test3.addAtHead(1)
#print(test3.head.val, test3.get(1), test3.get(2))
#test3.addAtIndex(3, 0)
#print(test3.head.val, test3.get(1), test3.get(2), test3.get(3))
#test3.deleteAtIndex(2)
#print(test3.head.val, test3.get(1), test3.get(2))
#test3.addAtHead(6)
#print(test3.head.val, test3.get(1), test3.get(2), test3.get(3))
#test3.addAtTail(4)
#print(test3.head.val, test3.get(1), test3.get(2), test3.get(3), test3.get(4))
#print(test3.get(4))
#test3.addAtHead(4)
#print(test3.head.val, test3.get(1), test3.get(2), test3.get(3), test3.get(4), test3.get(5))
#test3.addAtIndex(5, 0)
#print(test3.head.val, test3.get(1), test3.get(2), test3.get(3), test3.get(4), test3.get(5), test3.get(6))
#test3.addAtHead(6)
#print(test3.head.val, test3.get(1), test3.get(2), test3.get(3), test3.get(4), test3.get(5), test3.get(6), test3.get(7))

#test4 = MyLinkedList()
#test4.addAtHead(1)
#print(test4.head.val)
#test4.addAtTail(3)
#print(test4.head.val, test4.get(1))
#test4.addAtIndex(1, 2)
#print(test4.head.val, test4.get(1), test4.get(2))
#print(test4.get(1))
#test4.deleteAtIndex(0)
#print(test4.head.val, test4.get(1))
#print(test4.get(0))

#test5 = MyLinkedList()
#test5.addAtIndex(0, 10)
#print(test5.head.val)
#test5.addAtIndex(0, 20)
#print(test5.head.val, test5.get(1))
#test5.addAtIndex(1, 30)
#print(test5.head.val, test5.get(1), test5.get(2))
#print(test5.get(0))

#test6 = MyLinkedList()
#test6.addAtTail(1)
#print(test6.get(0))

#test7 = MyLinkedList()
#test7.addAtHead(2)
#print(test7.head.val)
#test7.deleteAtIndex(1)
#test7.addAtHead(2)
#print(test7.head.val)
#test7.addAtHead(7)
#print(test7.head.val, test7.get(1))
#test7.addAtHead(3)
#print(test7.head.val, test7.get(1), test7.get(2))
#test7.addAtHead(2)
#print(test7.head.val, test7.get(1), test7.get(2), test7.get(3))
#test7.addAtHead(5)
#print(test7.head.val, test7.get(1), test7.get(2), test7.get(3), test7.get(4))
#test7.addAtHead(5)
#print(test7.head.val, test7.get(1), test7.get(2), test7.get(3), test7.get(4), test7.get(5))
#print(test7.get(5))
#test7.deleteAtIndex(6)
#test7.deleteAtIndex(4)

#test4 = (["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"], [[], [1], [3], [1, 2], [1], [0], [0]])
#
#def test(*args):
#    count = 1
#
#    def run():
#        for test in args:
#            nonlocal count
#            print('~ test', count)
#
#            actions, values = test
#            test_LL = eval('{}()'.format(actions[0]))
#
#            for i in range(1, len(actions)):
#                eval('{}.{}({})'.format(test_LL, actions[i], *values[i]))
#                
#                curr = test_LL.head
#                while curr is not None:
#                    print(curr.val)
#                    curr = curr.next
#
#    return run()
#
#
#test(test4)


## LeetCode Solutions
#########################

## Approach 1: Singly Linked List
#####################################
# time: O(1) - addAtHead
#       O(k) - get, addAtIndex, deleteAtIndex, where k is index of element
#       O(n) - addAtTail
# space: O(1) - for all operations
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next


## Approach 2: Doubly Linked List
#####################################
# time: O(1) - addAtHead, addAtTail
#       O(min(k, n - k)) - get, addAtIndex, deleteAtIndex, where k is the
#                          index of element to get, add or delete
# space: O(1) - for all operations
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        # choose the fastest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
                
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        # insertion itself
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        # delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred


## Starting Prompt
######################
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        

