# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        queue.append(root)

        while queue:
            level_order = []
            for _ in range(len(queue)):
                element = queue.popleft()
                if element:
                    level_order.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)

            res.append(level_order)
        return res[:len(res) - 1]

