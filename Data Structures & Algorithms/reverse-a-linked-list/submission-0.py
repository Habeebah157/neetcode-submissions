# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        prev = None
        temp = head
        nextNode = temp.next

        while nextNode:
            temp.next = prev
            prev = temp
            temp = nextNode
            nextNode = nextNode.next
        temp.next = prev
        return temp
        