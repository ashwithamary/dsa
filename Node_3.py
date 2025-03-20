class Node_3:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    max = head.value
    current = head
    while current:
        if current.value>=max:
            max = current.value
        current = current.next
    
    return max

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next
    current.next = None 
    return head

head = Node_3("Isabelle", Node_3("Alfonso", Node_3("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

# pb 1
# head1 = Node_3(5, Node_3(6, Node_3(7, Node_3(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node_3(5, Node_3(8, Node_3(6, Node_3(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))
