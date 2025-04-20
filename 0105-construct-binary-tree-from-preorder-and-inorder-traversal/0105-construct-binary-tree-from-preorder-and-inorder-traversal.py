class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)
            index = idx_map[val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root
        return helper(0, len(inorder) - 1)
