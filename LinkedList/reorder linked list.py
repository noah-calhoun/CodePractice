
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

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

    def reorderList(self, head: Optional[ListNode]) -> None:

        return


    def reorderListOld(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Too slow, but works
        """
        if not head or not head.next:
            return

        dummy = current = ListNode()
        dummy.next = head
        left = 0
        headSize = self.getCountOld(head)

        while left < headSize:
            if left % 2 == 0:
                if left > 0:
                    head = head.next
                left += 1
            else:
                current = head
                while current.next != None:
                    current = current.next
                left += 1
                current.next = None
                temp = head.next
                head.next = current
                head = head.next
                head.next = temp
                current = head
                for i in range(headSize - left):
                    current = current.next
                current.next = None

    def getCountOld(self, head: ListNode) -> int:
        temp = head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count


    

if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    list1 = create_linked_list(list1)
    sol = Solution()
    merged_list = sol.reorderList(list1)