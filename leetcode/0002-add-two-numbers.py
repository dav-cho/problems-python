##
#### Add Two Numbers (medium)
#################################

# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the
# two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any
# leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number
# that does not have leading zeros.

################################################################################


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     sentinel_head = ListNode()
#     current = sentinel_head
#     carry = 0

#     while l1 or l2 or carry:
#         val1 = l1.val if l1 else 0
#         val2 = l2.val if l2 else 0
#         sum = carry + val1 + val2
#         carry, digit_sum = divmod(sum, 10)

#         current.next = ListNode(digit_sum)
#         current = current.next
#         l1 = l1.next if l1 else None
#         l2 = l2.next if l2 else None

#     return sentinel_head.next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    current = sentinel_head = ListNode()
    carry = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = carry + val1 + val2
        if sum >= 10:
            carry = 1
            sum -= 10
        else:
            carry = 0

        current.next = ListNode(sum)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry == 1:
        current.next = ListNode(1)

    return sentinel_head.next


# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     current = ListNode()
#     head = ListNode(l1.value + l2.value, next=None)
#     current.next = head
#     sum = 0
#     carry = 0
#     current_index = 0

#     while l1 or l2 or carry:
#         temp_sum = l1.val + l2.val
#         digit_sum = temp_sum % 10
#         carry = temp_sum // 10

#         sum += digit_sum
#         l1, l2 = l1.next, l2.next
#         current_index += 1


# Approach 1: Elementary Math
# --------------------------
# Initialize current node to dummy head of the returning list.
# Initialize carry to 00.
# Initialize pp and qq to head of l1l1 and l2l2 respectively.
# Loop through lists l1l1 and l2l2 until you reach both ends.
#   - Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
#   - Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
#   - Set sum = x + y + carrysum=x+y+carry.
#   - Update carry = sum / 10carry=sum/10.
#   - Create a new node with the digit value of (sum \bmod 10)(summod10)
#     and set it to current node's next, then advance current node to next.
#   - Advance both pp and qq.
# Check if carry = 1carry=1, if so append a new node with
# digit 11 to the returning list.
# Return dummy head's next node.
# Note that we use a dummy head to simplify the code.
# Without a dummy head, you would have to write extra conditional
# statements to initialize the head's value.
# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     dummy_head = ListNode()
#     current = dummy_head
#     carry = 0

#     while l1 and l2 and carry:
#         value1 = l1.value if l1 else 0
#         value2 = l2.value if l2 else 0

#         sum = carry + value1 + value2
#         carry, digit_sum = divmod(sum, 10)
#         print("~ divmod", carry, digit_sum)

#         current.next = ListNode(digit_sum)
#         current = current.next

#         l1 = l1.next if l1 else None
#         l2 = l2.next if l2 else None

#     return dummy_head.next
