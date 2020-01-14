# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        lenA = self.length(curA)
        lenB = self.length(curB)

        # padding
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        elif lenA < lenB:
            for _ in range(lenB - lenA):
                curB = curB.next

        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next

        # return None

    def length(self, head):
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt
