# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(len(head))
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            head = head.next


if __name__ == '__main__':
    head = [1,1,2,3,3]
    sol = Solution()
    print(sol.deleteDuplicates(ListNode(head)))