# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        leading = 0
        dummy = cur = ListNode(0)
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = (a + b + leading) % 10
            leading = (a + b + leading) // 10
            cur.next = ListNode(sum)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry != 0:
            cur.next = ListNode(carry)
            
        return dummy.next