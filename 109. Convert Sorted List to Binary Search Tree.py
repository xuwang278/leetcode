# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)


        slow = fast = head
        last = None
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        last.next = None
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast)

        return root


        