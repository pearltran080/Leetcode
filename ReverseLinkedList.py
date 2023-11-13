# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        newHead = head
        prevNode = None

        while newHead is not None:
            next = newHead.next
            newHead.next = prevNode
            prevNode = newHead
            newHead = next

        return prevNode

#not