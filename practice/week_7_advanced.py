# pb 1
# def count_layers(sandwich):
#     if not sandwich:
#         return 0
#     if len(sandwich)==1:
#         return 1
#     return 1 + count_layers(sandwich[1])

# sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
# sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))


# pb 2

# def reverse_orders(orders):
#     if " " not in orders:
#         return orders
    
#     first_space_index = orders.find(" ")
#     first_order = orders[:first_space_index]
#     remaining_orders = orders[first_space_index + 1:]

#     return reverse_orders(remaining_orders) + " " + first_order

# print(reverse_orders("Bagel Sandwich Coffee"))


# pb 3
# find the sum of all batches of coffees
# check if that can be divided equally among n
# if yes true, if not false

# def can_split_coffee(coffee, n):
#     total = helper(coffee,0)
#     if total%n==0:
#         return True
#     else:
#         return False

# def helper(coffee, total):
#     if len(coffee)==0:
#         return total
#     total+=coffee[0]
#     return helper(coffee[1:],total)
    
# print(can_split_coffee([4, 4, 8], 2))
# print(can_split_coffee([5, 10, 15], 4))


# pb 4
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

# def merge_orders(sandwich_a, sandwich_b):
#     if not sandwich_a:
#         return sandwich_b
#     if not sandwich_b:
#         return sandwich_a
    
#     head = sandwich_a
#     current_a = sandwich_a
#     current_b = sandwich_b

#     while current_a and current_b:
#         next_a = current_a.next
#         next_b = current_b.next
        
#         current_a.next = current_b
#         if next_a: 
#             current_b.next = next_a
        
#         current_a = next_a
#         current_b = next_b
    
#     if current_b:
#         last = head
#         while last.next:
#             last = last.next
#         last.next = current_b
#     return head


# sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
# sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
# sandwich_c = Node('Bread')

# # print_linked_list(merge_orders(sandwich_a, sandwich_b))
# print_linked_list(merge_orders(sandwich_a, sandwich_c))


# pb 6
def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # True expression
            stack.pop()  # Remove the ':'
            false_expr = stack.pop()  # False expression
            
            if char == 'T':
                stack.append(true_expr)
            else:
                stack.append(false_expr)
        else:
            stack.append(char)
    
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    pass

