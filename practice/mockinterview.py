class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_node(head,value):
    if not head:
        return None
    
    slow= head
    fast= head
    current = head

    while slow and slow.val == value:
        slow.next

    while fast and fast.next:
        if fast.val !=value:
            

        if current!=value:
            slow=slow.next
            fast = fast.next.next
        else:
            slow=slow.next
            fast=fast.next
        current= current.next

    return slow

1 2 3 4 5 5 6 5
5
1 2 3 4 6

# 1,2,3,4,5,6
# fast 1,3,5,None
# slow 1,2,3,4

# 1,2,3,4,5