# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # First pass: count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # Find the target node (1-indexed from start)
        target = count - n
        
        # Move to the node just before the target
        curr = dummy
        for _ in range(target):
            curr = curr.next
        
        # Remove the target node
        curr.next = curr.next.next
        
        return dummy.next