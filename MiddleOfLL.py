# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        lst = []
        move = head
        while (move != None):
            lst.append(move.val)
            move = move.next
        count = (len(lst)//2)

        move = head
        for i in range(count):
            move = move.next
        return move
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
