# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        largest_diameter = [0]

        def height(root):
            if not root:
                return 0
            
            left_hgt = height(root.left)
            right_hgt = height(root.right)

            diameter = left_hgt + right_hgt

            largest_diameter[0] = max(largest_diameter[0],diameter)
            return 1 + max(left_hgt , right_hgt)

        height(root)
        return largest_diameter[0]