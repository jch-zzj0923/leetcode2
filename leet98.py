class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = -float('inf')

    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val<=self.pre:
            return False
        self.pre=root.val
        return self.isValidBST(root.right) 
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    solution = Solution()
    is_valid_bst = solution.isValidBST(root)
    print( is_valid_bst)
             