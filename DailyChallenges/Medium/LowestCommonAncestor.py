#1123. Lowest Common Ancestor of Deepest Leaves
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform a depth-first search on the tree.
        def dfs(node):
            if not node:
                return (None, 0)
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            elif right_depth > left_depth:
                return (right_lca, right_depth + 1)
            else:
                return (node, left_depth + 1)

        # Call the DFS helper function and return the lowest common ancestor.
        return dfs(root)[0]
