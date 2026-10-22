class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        cur=root
        while res or cur:
            while cur:
                res.append(cur)
                cur=cur.left
            cur=res.pop()
            k-=1
            if k==0:
                return cur.val
            cur=cur.right
if __name__ == "__main__":
    s=Solution()
    root=TreeNode(3)
    root.left=TreeNode(1)
    root.right=TreeNode(4)
    root.left.right=TreeNode(2)
    print(s.kthSmallest(root,1))