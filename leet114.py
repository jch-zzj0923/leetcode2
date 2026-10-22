from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        cur=root
        while cur:
            if cur.left :
                tail=cur.left
                while tail.right:
                    tail=tail.right
                tail.right=cur.right
                cur.right=cur.left
                cur.left=None
            cur=cur.right
if __name__=="__main__":
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(5)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(4)
    root.right.right=TreeNode(6)
    s.flatten(root)
    q=deque([root])
    while q:
        node=q.popleft()
        print(node.val,end=" ")
        if node.right:
            q.append(node.right)            

