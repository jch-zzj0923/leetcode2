from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self,p:Optional[TreeNode],q:Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val==q.val and self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
    def isSymmetric(self, root: TreeNode | None) -> bool: 
        return self.isSameTree(root.left,root.right)
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    solution = Solution()
    inverted_root = solution.isSymmetric(root)
    print(inverted_root)
