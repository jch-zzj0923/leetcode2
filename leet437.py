from typing import Optional
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        record=defaultdict(int)
        record[0]=1
        def dfs(node,pre_sum):
            if not node:
                return 0
            pre_sum+=node.val
            res=record[pre_sum-targetSum]
            record[pre_sum]+=1
            res+=dfs(node.left,pre_sum)
            res+=dfs(node.right,pre_sum)
            record[pre_sum]-=1
            return res
        return dfs(root,0)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    solution = Solution()
    result = solution.pathSum(root, 8)
    print(result)  # Output: 3