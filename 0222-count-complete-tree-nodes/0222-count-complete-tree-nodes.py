class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth

        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)

        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)
