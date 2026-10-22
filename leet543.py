from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.node_max=0
        def de_depth(node):
            if  node is None:
                return 0
            left=de_depth(node.left)
            right=de_depth(node.right)
            self.node_max=max(self.node_max,left+right)
            return max(left,right)+1
        de_depth(root)
        return self.node_max
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)
    print(diameter)