class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    slow = path_start
    fast = path_start
    isCycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            #return slow.value
            isCycle = True
            break
    if isCycle:
        slow = path_start
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.value     
    return None


path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))
