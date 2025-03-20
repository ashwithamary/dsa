class Node_2:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_racers(head):
    res = 0
    current = head
    while current:
        res+=1
        current=current.next
    
    return res

def last_place(head):
    if head is None:
        return None
    current = head
    while current.next:
        current=current.next
    return current.value

def increment_rank(head, target):
    if target <= 1 or head is None or head.next is None:
        return head

    index = 1
    prev = None
    current = head

    while index < target:
        prev = current
        current = current.next
        index += 1

    temp = prev.value
    prev.value = current.value
    current.value = temp

    return head 


# pb 8
racers1 = Node_2("Mario", Node_2("Peach", Node_2("Luigi", Node_2("Daisy"))))
racers2 = Node_2("Mario", Node_2("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 

# pb 7
# racers1 = Node_2("Mario", Node_2("Peach", Node_2("Luigi", Node_2("Daisy"))))
# racers2 = Node_2("Mario")

# print(last_place(racers1)) 
# print(last_place(racers2)) 
# print(last_place(None))

# pb 6
# racers1 = Node_2("Mario", Node_2("Peach", Node_2("Luigi", Node_2("Daisy"))))
# racers2 = Node_2("Mario")

# print(count_racers(racers1))
# print(count_racers(racers2))
# print(count_racers(None))

# pb 5
# daisy = Node_2("Daisy")
# peach = Node_2("Peach")
# luigi = Node_2("Luigi")
# mario = Node_2("Mario")

# # Add code here to link the above Node_2s
# daisy.next = peach
# peach.next = luigi
# luigi.next = mario


# print_linked_list(daisy)
