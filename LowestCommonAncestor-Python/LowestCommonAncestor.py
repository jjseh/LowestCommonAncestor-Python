#
#           Binary Tree
#
#                 4
# 	          |
#         +-------+-------+
#         |		  |
# 	 10               7
# 	  |               |
#     +---+---+       +---+---+
#     |       |       |       |
#     2       3       5       1
#   +-+-+   +-+-+   +-+-+   +-+-+
#   |   |   |   |   |   |   |   |
#   8   9   6   14  12  15  11  16
#
#

#A binary tree node
class Nodes:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = Nodes(4);
root.left = Nodes(10);
root.right = Nodes(7);
root.left.left = Nodes(2);
root.left.right = Nodes(3);
root.right.left = Nodes(5);
root.right.right = Nodes(1);
root.left.left.left = Nodes(8);
root.left.left.right = Nodes(9);
root.left.right.left = Nodes(6);
root.left.right.right = Nodes(14);
root.right.left.left = Nodes(12);
root.right.left.right = Nodes(15);
root.right.right.left = Nodes(11);
root.right.right.right = Nodes(16);


# Find Lowest Common Ancestor and return if both given nodes are found
def findLowestCommonAncestor(root, node1, node2):
    # Base Case
    if root is None:
        return None

    if root.key == node1 or root.key == node2:
        return root

    leftSubtreeLca = findLowestCommonAncestor(root.left, node1, node2)
    rightSubtreeLca = findLowestCommonAncestor(root.right, node1, node2)

    if leftSubtreeLca and rightSubtreeLca:
        return root

    return leftSubtreeLca if leftSubtreeLca is not None else rightSubtreeLca


print("Lowest Common Ancestor of 8 and 9: = ", findLowestCommonAncestor(root, 8, 9, ).key)
print("Lowest Common Ancestor of 7 and 5:= ", findLowestCommonAncestor(root, 7, 5).key)
print("Lowest Common Ancestor of 11 and 16: = ", findLowestCommonAncestor(root, 11, 16).key)
print("Lowest Common Ancestor of 10 and 7: = ", findLowestCommonAncestor(root, 10, 7).key)
print("Lowest Common Ancestor of 12 and 15: = ", findLowestCommonAncestor(root, 12, 15).key)
