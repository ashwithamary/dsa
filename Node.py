# # pb 5
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# # Add code here to link the above nodes
# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# # pb 5
# print_linked_list(kk_slider)


class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head != None:
        print("I caught a",head.fish_name)
        return head.next
    else:
        print("Aw! Better luck next time!")
        return None

def fish_chances(head, fish_name):
    total = 0
    count = 0
    current = head
    while current:
        total +=1
        if current.fish_name == fish_name:
            count+=1
        current = current.next
        
    return round(count/total,2)

def restock(head, new_fish):
    new_node = Node(new_fish)

    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# pb 6
# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

# pb 7
# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

# pb 8
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))
