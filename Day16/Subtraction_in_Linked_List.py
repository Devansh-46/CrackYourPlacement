def length(n):
    ret = 0
    while n:
        ret+=1
        n = n.next
    return ret

def reverse(head):
    # this function reverses the linked list
    prev = None
    current = head
    next = None
    
    while current is not None:
        next = current.next      # storing next node
        current.next = prev      # linking current node to previous
        prev = current           # updating prev
        current = next           # updating current
    
    return prev

class Solution:    
    def subLinkedList(self, l1, l2):
        
        while l1 is not None and l1.data==0:
            l1 = l1.next
            # removing trailing zeroes from l1
        
        while l2 is not None and l2.data==0:
            l2 = l2.next
            # removing trailing zeroes from l2
        
        n1 = length(l1)
        n2 = length(l2)
        
        if n1 == 0 and n2 == 0:
            return Node(0)
        
        if(n2>n1):
            l1 , l2 = l2 , l1
            # making sure l1 list has the bigger number
        
        if n1==n2:
            t1=l1
            t2=l2
            while t1.data == t2.data:
                # finding which number is greater
                t1 = t1.next
                t2 = t2.next
                
                if t1 is None:
                    return Node(0)
                    # returning zero if both numbers are same
            
            if t2.data > t1.data:
                l1 , l2 = l2 , l1
                # making sure l1 list has the bigger number
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        res = None
        t1 = l1
        t2 = l2
        while t1 is not None:
            small = 0
            if t2 is not None:
                small = t2.data
                # 'small' holds the next digit of number to be subtracted
            
            if t1.data < small:
                t1.next.data -= 1
                t1.data += 10
                # taking carry
            
            n = Node( t1.data - small )
            # creating new node for storing difference
            n.next = res
            res = n
            
            t1 = t1.next
            if t2 is not None:
                t2 = t2.next
        
        while res.next is not None and res.data==0:
            res = res.next
            # removing trailing zeroes from result list
        
        return res
