# Given the head of a linked list, remove the nth node from the end of the list and return its head.



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0, head)
        left = dummy
        for i in range(n): current = current.next 
        
        while current:
            current = current.next
            left = left.next
        left.next = left.next.next

        return dummy.next








if __name__ == '__main__':
    # head = [1,2,3,4,5]
    # n = 2
    head = [1,2]
    n = 1
    list1 = create_linked_list(head)
    sol = Solution()
    merged_list = sol.removeNthFromEnd(list1, n)