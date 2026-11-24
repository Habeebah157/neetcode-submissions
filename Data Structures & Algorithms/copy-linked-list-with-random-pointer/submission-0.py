"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        each contains a random which may point to any node in the list. 
        exactly n new node
        --- Original value
        --- A next pointer
        --- A random pointer
        return the head of the copied linked list

        '''
        if not head:
            return None

        # Step 1: Store next and random for each node
        copy = defaultdict(list)
        curr = head
        while curr:
            copy[curr] = [curr.next, curr.random]
            curr = curr.next

        # Step 2: Create a mapping: original node -> new node
        newconnection = {}
        curr = head
        while curr:
            newconnection[curr] = Node(curr.val)  # one copy per original
            curr = curr.next

        # Step 3: Build the new list and set random pointers
        dummy = Node(0)
        secondhead = dummy

        for original_node, (next_node, random_node) in copy.items():
            # Create the new node (but reuse from newconnection)
            new_node = newconnection[original_node]
            secondhead.next = new_node
            secondhead = secondhead.next

            # ✅ Now set the random pointer correctly
            if random_node is not None:
                secondhead.random = newconnection[random_node]
            # else: remains None

        return dummy.next