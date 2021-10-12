import unittest
from LowestCommonAncestor import findLowestCommonAncestor, Nodes

# Lowest Common Ancestor
#
#
#           Binary Tree
#
#                 4
# 				  |
# 		  +-------+-------+
# 		  |				  |
# 		 10               7
# 		  |	              |
# 	  +---+---+       +---+---+
# 	  |       |       |       |
# 	  2       3       5       1
#   +-+-+   +-+-+   +-+-+   +-+-+
#   |   |   |   |   |   |   |   |
#   8   9   6   14  12  15  11  16
#


class MyTestCase(unittest.TestCase):
    def testLCA(self):
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
        nullroot = None

        # No Node Test
        self.assertEqual(None, findLowestCommonAncestor(nullroot, 20, 19))

        # Test available nodes
        self.assertEqual(2, findLowestCommonAncestor(root, 8, 9).key)
        self.assertEqual(7, findLowestCommonAncestor(root, 7, 5).key)
        self.assertEqual(1, findLowestCommonAncestor(root, 11, 16).key)
        self.assertEqual(4, findLowestCommonAncestor(root, 10, 7).key)
        self.assertEqual(5, findLowestCommonAncestor(root, 12, 15).key)

        # Test same nodes
        self.assertEqual(12, findLowestCommonAncestor(root, 12, 12).key)

        # Test common LCA
        self.assertEqual(4, findLowestCommonAncestor(root, 4, 8).key)
        self.assertEqual(4, findLowestCommonAncestor(root, 4, 16).key)
        self.assertEqual(4, findLowestCommonAncestor(root, 8, 16).key)



if __name__ == '__main__':
    unittest.main()
