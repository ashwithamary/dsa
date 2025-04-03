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

def can_split_coffee(coffee, n):
    total = helper(coffee,0)
    if total%n==0:
        return True
    else:
        return False

def helper(coffee, total):
    if len(coffee)==0:
        return total
    total+=coffee[0]
    return helper(coffee[1:],total)
    
print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
