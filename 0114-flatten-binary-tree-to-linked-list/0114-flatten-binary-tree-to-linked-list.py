class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            right_subtree = root.right
            root.right = root.left
            root.left = None

            current = root.right
            while current.right:
                current = current.right
            current.right = right_subtree
