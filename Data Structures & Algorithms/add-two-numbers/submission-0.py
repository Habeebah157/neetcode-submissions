# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def list_to_listnode(lst):
    if not lst:
        return None

    # Initialize the head of the linked list
    head = ListNode(lst[0])
    current = head

    # Iterate over the rest of the list and create nodes
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next

    return head
def list_to_linkedlist(lst):
    linkedlist = ListNode()
    for item in lst:
        linkedlist.append(item)
    return linkedlist

class Solution:
   
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        list1, list2 = [], []
        while curr1 and curr2:
            list1.append(curr1.val)
            list2.append(curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        if curr1 != None: 
            while(curr1):
                list1.append(curr1.val)
                curr1 = curr1.next
        if curr2 != None:
            while(curr2):
                list2.append(curr2.val)
                curr2 = curr2.next
        suml1, suml2 = 0, 0
        for i in range(len(list1)-1, -1, -1):
            suml1 = ''.join(str(num) for num in list1)
        for i in range(len(list2)-1, -1, -1):
            suml2 = ''.join(str(num) for num in list2)
        rterm1 = suml1[::-1]
        rterm2 = suml2[::-1]
        rterm1 = int(rterm1)
        print(rterm1)
        print(rterm2)
        rterm2 = int(rterm2)
        total = str(rterm1 + rterm2)
        print(total)
        total = total[::-1]
        digit_list = [int(digit) for digit in str(total)]
        print(digit_list)

        final = list_to_listnode(digit_list)
        return final
       

    
        