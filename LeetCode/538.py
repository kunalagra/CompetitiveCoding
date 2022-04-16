# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum1=0
        def inorder(root):
            nonlocal sum1
            if root!=None:
                inorder(root.right)
                sum1+=root.val
                root.val=sum1
                inorder(root.left)
        inorder(root)
        return root