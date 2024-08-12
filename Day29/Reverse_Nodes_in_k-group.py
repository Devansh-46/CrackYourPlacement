# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return None

        if k == 1: 
            return head

        end_check = head        
        for _ in range(k-1):
            if not end_check.next: 
                return head
            end_check = end_check.next
        
        # if not end_check: return head

        blank = ListNode(0)
        p0, p1, count = blank, head, 0

        while count < k:
            curr = p1
            p2 = curr.next
            curr.next = p0
            p0 = p1
            p1 = p2
            count += 1

        head.next = self.reverseKGroup(p2, k)
        head = p0

        return head
        
