# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        UMPIRE
        beginning linked list and array integer. 
        Remove nth node from the end of the list. 

        [1, 2, 3, 4]
        [1, 2, 4]
        [5]
        [1,2]
        edge: empty, n = 1 or more

        [1 2 3 4]
               |
        4 - 2 = 2
           |


         [5 2]
         |
        if curr.next.next: 
            curr.next = curr.next.next
        else: 
            curr.next  = None
        [5]
         |
    
        count = 0
        curr = head
        while curr: 
            count += 1
            curr = curr.next

        count = count - n
        curr = head

        if count = 0 and not curr.next: 
            return None
        else: 
            return head.next
        
        tracker = 0
        curr = head
        while tracker < count-1: 
            curr = curr.next
            tracker += 1

        if curr.next.next: 
            curr.next = curr.next.next
        else: 
            curr.next  = None

        return head


        '''


        count = 0
        curr = head
        while curr: 
            count += 1
            curr = curr.next

        count = count - n 
        curr = head
        print("count", count)

        if count == 0 and not curr.next: 
            print("YES")
            return None
        elif count == 0: 
            return head.next
        tracker = 0
        curr = head
        
        while tracker < count - 1: 
            curr = curr.next
            tracker += 1

        if curr.next.next: 
            curr.next = curr.next.next
        else: 
            curr.next = None

        return head
        