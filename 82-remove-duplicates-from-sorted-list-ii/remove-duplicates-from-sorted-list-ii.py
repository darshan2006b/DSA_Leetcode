# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        dummy = ListNode()
        curr = dummy
        h = {}

        while cur:
            h[cur.val] = h.get(cur.val,0) + 1
            cur = cur.next

        cur = head

        while cur:
            if h[cur.val] == 1:
                curr.next = cur                
                curr = curr.next
            cur = cur.next
            curr.next = None
        return dummy.next