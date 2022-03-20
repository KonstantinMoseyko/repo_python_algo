"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root: return None

        nodes_at_each_level = []
        level = [root]

        while level:
            nodes_at_each_level.append([node for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]

        # return root

        for level_nodes in nodes_at_each_level:
            for idx in range(len(level_nodes) - 1):
                level_nodes[idx].next = level_nodes[idx + 1]

        return root

