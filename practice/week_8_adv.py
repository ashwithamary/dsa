from collections import deque 
from collections import defaultdict

class TreeNode:
    def __init__(self, val, key=None, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# def sort_plants(collection):
#     result = []

#     def inorder(node):
#         if node:
#             inorder(node.left)
#             result.append((node.key, node.val))
#             inorder(node.right)

#     inorder(collection)
#     return result


# """
#          (3, "Monstera")
#         /               \
#    (1, "Pothos")     (5, "Witchcraft Orchid")
#         \                 /
#   (2, "Spider Plant")   (4, "Hoya Motoskei")
# """

# # Using build_tree() function at the top of page
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


# def find_flower(inventory, name):
#     if inventory is None:
#         return False
    
#     if inventory.val == name:
#         return True
#     elif name < inventory.val:
#         return find_flower(inventory.left, name)
#     else:
#         return find_flower(inventory.right, name)



# """
#          Rose
#         /    \
#       Lily   Tulip
#      /  \       \
#   Daisy  Lilac  Violet
# """



# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

# def add_plant(collection, name):
#     if not collection:
#         return TreeNode(name)

#     if name < collection.val:
#         collection.left = add_plant(collection.left, name)
#     else:
#         collection.right = add_plant(collection.right, name)

#     return collection

# def right_most_node(node):
#     current = node
#     while current.right:
#         current=current.right
#     return current

# def remove_plant(collection, name):
#     if not collection:
#         return collection

#     if name < collection.val:
#         collection.left = remove_plant(collection.left, name)
#     elif name> collection.val:
#         collection.right = remove_plant(collection.right, name)
#     else:
#         if collection.left==None and collection.right==None:
#             return None

#         if collection.left==None:
#             return collection.right
#         if collection.right==None:
#             return collection.left
        
#         pred = right_most_node(collection.left)

#         collection.val = pred.val

#         collection.left = remove_plant(collection.left, pred.val)
#     return collection


# # using build_tree() function at top of page
# values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
# garden = None
# for flower in values:
#     if flower is not None:  
#         garden = insert_bst(garden, flower)

# print_tree(remove_plant(garden, "Pilea"))


def find_most_common(root):
    frequencyMap = defaultdict(int)

    def inorder(node, frequencyMap):
        if node:
            inorder(node.left, frequencyMap)
            frequencyMap[node.val] += 1
            inorder(node.right, frequencyMap)

    inorder(root, frequencyMap)

    max_count = max(frequencyMap.values())

    return [val for val, count in frequencyMap.items() if count == max_count]


"""
    Hoya
      \ 
      Pothos
      /
    Pothos
"""

# Using build_tree() function at top of page
values = ["Hoya", None, "Pothos", "Pothos"]
collection1 = build_tree(values)

"""
      Hoya
    /      \ 
  Aloe    Pothos
  /        /
 Aloe   Pothos
"""
values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
collection2 = build_tree(values)

print(find_most_common(collection1))
print(find_most_common(collection2))
