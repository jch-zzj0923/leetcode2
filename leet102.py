from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans=[]
        cur=[root]
        while cur:
            nex=[]
            vals=[]
            for node in cur:
                vals.append(node.val)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            cur=nex
            ans.append(vals)
        return ans
                
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    level_order_result = solution.levelOrder(root)
    print(level_order_result)  # Output: [[1], [2, 3], [4, 5, 6, 7]]