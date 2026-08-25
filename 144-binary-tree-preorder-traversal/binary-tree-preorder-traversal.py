# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        def pre(root):
            if not root:
                return []
            stk = []
            stk.append(root)
            while stk:
                node = stk.pop()
                ans.append(node.val)
                if node.left : pre(node.left)
                if node.right : pre(node.right)
                
        pre(root)
        return ans