

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        def build(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=build(l,mid-1)
            root.right=build(mid+1,r)
            return root
        return build(0,len(nums)-1)
if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    root = solution.sortedArrayToBST(nums)