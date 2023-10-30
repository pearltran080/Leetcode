# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        # holds the previous node
        prev = head

        # holds the final head node
        result = prev

        while head is not None:
            if head.val == val:
                prev.next = head.next   # the previous node's next will no longer be the current node
                head = head.next
            else:
                prev = head
                head = head.next

            if result.val == val:
                result = head

        return result
