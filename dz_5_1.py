"""
145. Binary Tree Postorder Traversal
"""

"""Definition for a binary tree node."""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(TreeNode):
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        output = []
        stack_mem = []
        if not root:
            return output
        stack_mem.append(root)
        stack_mem.append(root)
        while (stack_mem):
            current = stack_mem.pop()
            if(stack_mem and current == stack_mem[-1]):
                if (current.right):
                    stack_mem.append(current.right)
                    stack_mem.append(current.right)
                if (current.left):
                    stack_mem.append(current.left)
                    stack_mem.append(current.left)
            else:
                output.append(current.val)
        return output


inputs = Solution()
print(inputs.postorderTraversal([1, 'null', 2, 3]))
