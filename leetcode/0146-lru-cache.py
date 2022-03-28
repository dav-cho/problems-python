##
#### 146. LRU Cache (medium)
################################


## ordered dictionary
##############################
import collections


class LRUCache(collections.OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


## hashmap + doubly linked list
###################################
class ListNode:
    def __init__(self, val=0, key=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.cache = {}
        self.size = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new = ListNode(value, key)
            self.cache[key] = new
            self._add_node(new)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self._move_to_head(node)
    
    def _add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        tail = self.tail.prev
        self._remove_node(res)
        return tail


## hashmap + doubly linked list 2
###################################
class ListNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.val = 0
        self.key = 0
        

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = ListNode()
            new_node.key = key
            new_node.val = value
            
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self._move_to_head(node)
        
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

