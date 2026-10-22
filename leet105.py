class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)
        idx=inorder.index(root_val)
        root.left=self.buildTree(preorder[1:1+idx],inorder[:idx])
        root.right=self.buildTree(preorder[1+idx:],inorder[1+idx:])
        return root
if __name__=="__main__":
    preorder=[3,9,20,15,7]
    inorder=[9,3,15,20,7]
    solution=Solution()
    root=solution.buildTree(preorder,inorder)
    def print_tree(node):
        if node:
            print(node.val,end=' ')
            print_tree(node.left)
            print_tree(node.right)
    print_tree(root)
