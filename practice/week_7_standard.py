# pb 1
#  def count_suits_iterative(suits):
#     length = 0
#     for suit in suits:
#         length+=1
    
#     return length

# def count_suits_recursive(suits):
#     if not suits:
#         return 0
#     return 1+ count_suits_recursive(suits[1:])


# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

# pb 2
# def sum_stones(stones):
#     if not stones:
#         return 0
#     return stones[0]+sum_stones(stones[1:])

# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

# pb 3
# def count_suits_iterative(suits):
#     unique_suits = set()
#     for suit in suits:
#         unique_suits.add(suit)
#     return len(unique_suits)

# def count_suits_recursive(suits):
#     if not suits:
#         return 0
#     first = suits[0]
#     rest_unique_ct = count_suits_recursive(suits[1:])
#     if first in suits[1:]:
#         return rest_unique_ct
#     else:
#         return 1+rest_unique_ct

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# pb 4
# def fibonacci_growth(n):
#     if n==0:
#         return 0
#     if n ==1:
#         return 1
#     else:
#         return fibonacci_growth(n-1)+fibonacci_growth(n-2)
    
# print(fibonacci_growth(5))
# print(fibonacci_growth(8))

# pb 5
# def power_of_four(n):
#     if n==0:
#         return 1
#     elif n>0:
#         return 4*power_of_four(n-1)
#     else:
#         return 1/(4*power_of_four(-n-1))
# print(power_of_four(2))
# print(power_of_four(-2))


# pb 6
# def strongest_avenger(strengths):
#     if len(strengths)==1:
#         return strengths[0]
#     else:
#         max_of_rest = strongest_avenger(strengths[1:])
#         return strengths[0] if strengths[0] > max_of_rest else max_of_rest

# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))


# pb 7
# def count_deposits(resources):
#     if not resources:
#         return 0
#     elif resources[0] =='V':
#         return 1+ count_deposits(resources[1:])
#     else:
#         return count_deposits(resources[1:])

# print(count_deposits("VVVVV"))
# print(count_deposits("VXVYGA"))

# pb 8
# class Node:
#   def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def merge_missions(mission1, mission2):
#     if not mission1:
#         return mission2
#     if not mission2:
#         return mission1
    
#     if mission1.value< mission2.value:
#         mission1.next = merge_missions(mission1.next, mission2)
#         return mission1
#     else:
#         mission2.next = merge_missions(mission2.next, mission1)
#         return mission2

# mission1 = Node(1, Node(2, Node(4)))
# mission2 = Node(1, Node(3, Node(4)))

# print_linked_list(merge_missions(mission1, mission2))


# pb 9
# class Node:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def merge_missions_iterative(mission1, mission2):
#     temp = Node()  # Temporary node to simplify the merging process
#     tail = temp

#     while mission1 and mission2:
#         if mission1.value < mission2.value:
#             tail.next = mission1
#             mission1 = mission1.next
#         else:
#             tail.next = mission2
#             mission2 = mission2.next
#         tail = tail.next

#     # Attach the remaining nodes, if any
#     if mission1:
#         tail.next = mission1
#     elif mission2:
#         tail.next = mission2

#     return temp.next  # Return the head of the merged linked list
