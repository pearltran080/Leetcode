# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        mover = l3
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                digit0 = l1.val
            else:
                digit0 = 0

            if l2 is not None:
                digit1 = l2.val
            else:
                digit1 = 0

            sum = digit0 + digit1 + carry
            value = sum % 10
            carry = sum // 10

            node = ListNode(value)
            mover.next = node
            mover = mover.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        result = l3.next
        return result
