class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res=[]
        def travel(node):
            if not node:
                return None
            travel(node.left)
            res.append(node.val)
            travel(node.right)
        travel(root)
        return res
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    print(sol.inorderTraversal(root))  # Output: [1, 3, 2]