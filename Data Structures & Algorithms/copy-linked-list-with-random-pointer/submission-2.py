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
        dummy= Node(x=0)
        curr_main = head
        curr_copy = dummy

        node_address = {}

        while curr_main:
            curr_copy.next = Node(x = curr_main.val)

            node_address[curr_main] = curr_copy.next

            curr_main = curr_main.next
            curr_copy = curr_copy.next
            

        curr_copy.next = None

        curr_main = head
        curr_copy = dummy.next

        while curr_main:
            if curr_main.random:
                curr_copy.random = node_address[curr_main.random]

            curr_main = curr_main.next
            curr_copy = curr_copy.next

        

        return dummy.next


        