# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        h ={}
        cur = head
        pos = 0
        while cur:
            if cur in h:
                return cur

            h[cur] = pos
            cur = cur.next
            pos += 1
            
        
