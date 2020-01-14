# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, more = ListNode(0), ListNode(0)
        l, m, cur = less, more, head
        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                m.next = cur
                m = m.next
                
            cur = cur.next
            
        l.next = more.next
        m.next = None
        return less.next
            