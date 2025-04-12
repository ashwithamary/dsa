from collections import deque 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# pb 8
def find_flower(root, flower):
    if root is None:
        return False
    if root.val == flower:
        return True

    return find_flower(root.left, flower) or find_flower(root.right, flower)

"""
         Rose
        /    \
       /      \
     Lily     Daisy
    /    \        \
Orchid  Lilac    Dahlia
"""

flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))


# pb 7
# def harvest_berries(root, threshold):
#     if root is None:
#         return 0
#     left_tree = harvest_berries(root.left, threshold)
#     right_tree = harvest_berries(root.right, threshold)
#     if root.val > threshold:
#         return root.val +left_tree+right_tree
#     else:
#         return left_tree+right_tree

# """
#        4
#      /   \
#    10     6
#   /  \     \
#  5    8    20
# """
# bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))

# pb 6
# def survey_tree(root):
#     if root is None:
#         return []
#     left_tree = survey_tree(root.left)
#     right_tree = survey_tree(root.right)

#     return left_tree+right_tree+[root.val]


# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# magnolia = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))


# pb 5
# def count_leaves(root):
#     if root is None:
#         return 0
    
#     if root.left == root.right ==None:
#         return 1

#     left_leaves = count_leaves(root.left)
#     right_leaves = count_leaves(root.right)

#     return left_leaves+right_leaves    


# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))

# pb 4
# def right_vine(root):
#     if not root:
#         return []
#     return [root.val] +right_vine(root.right)

# pb 3
# def right_vine(root):
#     arr = [root.val]
#     while root.right:
#         arr.append(root.right.val)
#         root.right = root.right.right
#     return arr

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# pb 2
# def calculate_yield(root):
#     if root.val == '+':
#         return root.left.val + root.right.val
#     elif root.val =='-':
#         return root.left.val - root.right.val
#     if root.val == '/':
#         return root.left.val / root.right.val
#     elif root.val =='*':
#         return root.left.val * root.right.val

# """
#     +
#   /   \
#  7     5
# """
# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))


# pb 1
# root = TreeNode("Trunk")
# root.left = TreeNode("Mcintosh")
# root.right = TreeNode("Granny Smith")
# root.left.left = TreeNode("Fuji")
# root.left.right = TreeNode("Opal")
# root.right.left = TreeNode("Crab")
# root.right.right = TreeNode("Gala")
# # Using print_tree() included at the top of this page
# print_tree(root)
