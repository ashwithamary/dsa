class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middleNode(head): 
    if head == None:
        return None
    fast = head
    slow = head
    cycle = False
    while (fast and fast.next):
        if slow==fast:
            cycle = True
        if (cycle):
            slow.next
        slow= slow.next
        fast= fast.next.next
    return slow

head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
slow = 1
fast = 1
print(middleNode(head))
head2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
print(middleNode(head2))

# Input: head = [1, 2, 3, 4, 5]
# Output: Node with value 3
# Input: head = [1, 2, 3, 4, 5, 6]
# Output: Node with value 4