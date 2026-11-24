# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = slow = head

        while fast.next and fast.next.next: 
            slow = slow.next
            fast = fast.next.next

        p2 = slow.next
        slow.next = None
        prev = None

        while p2: 
            next = p2.next
            p2.next = prev
            prev = p2
            p2 = next

        p1 = head
        p2 = prev

        while p2: 
            nextp1 = p1.next
            nextp2 = p2.next

            p1.next = p2
            p2.next = nextp1

            p1 = nextp1
            p2 = nextp2


        


        
        