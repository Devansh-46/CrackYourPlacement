class Solution:
    def compute(self, head):
        if head.next is None:
            return head

        head.next = self.compute(head.next)
        if head.data < head.next.data:
            return head.next
        
        return head
