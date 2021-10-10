# A binary tree node
class Nodes:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Find Lowest Common Ancestor and return if both given nodes are found
def findLowestCommonAncestor(root, node1, node2):
    # Base Case
    if root is None:
        return None


    if root.key == node1 or root.key == node2:
        return root

    # Check for keys in tree
    # Check left and right subtree
    leftSubtreeLca = findLowestCommonAncestor(root.left, node1, node2)
    rightSubtreeLca = findLowestCommonAncestor(root.right, node1, node2)


    if leftSubtreeLca and rightSubtreeLca:
        return root

    # Otherwise check if LCA is in hte right ot left subtree
    return leftSubtreeLca if leftSubtreeLca is not None else rightSubtreeLca

