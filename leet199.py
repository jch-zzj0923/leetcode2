from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        res=[]
        q=deque()
        q.append(root)
        while q:
            level=len(q)
            for i in range(level):
                node=q.popleft()
                if i == level-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
if __name__ == "__main__":
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(5)
    root.right.right=TreeNode(4)
    print(s.rightSideView(root))