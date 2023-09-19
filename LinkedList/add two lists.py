
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


from typing import Optional


def create_linked_list(values):
    if not values:
        return None

    # Create the first node from the first value
    head = ListNode(values[0])
    current = head

    # Create the rest of the nodes from the remaining values
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
    
    def addTwoNumbersOld(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        If its stupid but works.... its still stupid
        """


        vals1 = []
        vals2 = []
        dummy = head = ListNode()
        vals1Total = ""
        vals2Total = ""

        while l1:
            vals1.append(l1.val)
            l1 = l1.next
        while l2:
            vals2.append(l2.val)
            l2 = l2.next

        for char in vals1[::-1]:
            vals1Total += str(char)
        for char in reversed(vals2):
            vals2Total += str(char)
        total = int(vals1Total) + int(vals2Total)
        totals = [int(digit) for digit in str(total)]

        for i, val in reversed(list(enumerate(totals))):
            head.val = val
            if i != 0:
                head.next = ListNode()
                head = head.next 

        return dummy


if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    list1 = create_linked_list(l1)
    list2 = create_linked_list(l2)
    sol = Solution()
    merged_list = sol.addTwoNumbers(list1, list2)


