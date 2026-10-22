class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.res=float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_gain=max(dfs(node.left),0)
            right_gain=max(dfs(node.right),0)
            current_sum=node.val+left_gain+right_gain
            if current_sum >self.res:
                self.res=current_sum
            return node.val+max(left_gain,right_gain)
        dfs(root)
        return self.res
if __name__=="__main__":
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    print(s.maxPathSum(root))
