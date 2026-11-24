# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None or head.next.next == None:
            return False
        sdummy = ListNode()
        fdummy = ListNode()
        sdummy.next = head
        fdummy.next = head
        while(sdummy and fdummy.next):
            if fdummy == sdummy:
                return True
            sdummy = sdummy.next
            print(fdummy.next.val)
            fdummy = fdummy.next.next
            print(fdummy.val)
        return False