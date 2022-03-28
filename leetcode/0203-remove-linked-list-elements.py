##
#### 203. Remove Linked List Elements (easy)
################################################


## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## sentinel / dummy node
############################
class Solution:
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next


## sentinel 2
#################
class Solution:
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        dummy = curr = ListNode(0)
        dummy.next = head

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


## Tests
############

test1 = ([1, 2, 6, 3, 4, 5, 6], 6)  # [1, 2, 3, 4, 5]
test2 = ([], 1)  # []
test3 = ([7, 7, 7, 7], 7)  # []


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            count += 1

            linked_list, val = test

            if not linked_list:
                print("[]")
                continue

            head = ListNode(linked_list[0])
            current = head

            for i in range(1, len(linked_list)):
                current.next = ListNode(linked_list[i])
                current = current.next

            print_LL(head)
            solution = Solution()
            result = solution.remove_elements(head, val)
            print_LL(result)

    return run()


def print_LL(head):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(linked_list)


test(test1, test2, test3)
