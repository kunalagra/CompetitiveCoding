class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root,prev=None):
            if root!=None:
                r = inorder(root.left,root)
                root.left=None
                root.right=inorder(root.right,prev)
                return r
            else:
                return prev
        return inorder(root)