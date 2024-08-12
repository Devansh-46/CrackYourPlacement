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
        if not head:
            return None
        
        cur = head
        while cur:
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = cur.next.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        
        cur = head
        new_head = cur.next
        copy_cur = new_head
        while cur:
            cur.next = copy_cur.next
            if cur.next:
                copy_cur.next = cur.next.next
            else:
                copy_cur.next = None
            cur = cur.next
            copy_cur = copy_cur.next

        return new_head
