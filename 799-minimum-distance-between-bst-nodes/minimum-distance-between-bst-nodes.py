# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        prev = None
        min_dist = float('inf')
        if not root:
            return []
        stk = []
        cur = root
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            
            cur = stk.pop()
            cur_val = cur.val

            if prev is not None:
                diff = cur_val - prev_val
                min_dist = min(min_dist, diff)

            prev = cur
            prev_val = prev.val
            cur = cur.right
        return min_dist
        