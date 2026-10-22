class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root 
        elif left:
            return left
        else:
            return right
if __name__=="__main__":
    root=TreeNode(3)
    root.left=TreeNode(5)
    root.right=TreeNode(1)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)
    root.right.left=TreeNode(0)
    root.right.right=TreeNode(8)
    root.left.right.left=TreeNode(7)
    root.left.right.right=TreeNode(4)
    p=root.left
    q=root.left.right.right
    s=Solution()
    print(s.lowestCommonAncestor(root,p,q).val)