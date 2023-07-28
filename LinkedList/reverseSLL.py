


# Given the head of a singly linked list, reverse the list, and return the reversed list.



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        


        return prev




if __name__ == "__main__":
    node4 = ListNode(4, None)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    head = node1

    # Reverse the linked list
    solution = Solution()

    reversed_head = solution.reverseList(head)