/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        // create node head
        ListNode result;
        
        if (list1 == null && list2 != null) {
            return list2;
        }
        else if (list1 != null && list2 == null) {
            return list1;
        }
        else if (list1 == null && list2 == null) {
            return new ListNode().next;
        }
        
        else {
        
        if (list1.val <= list2.val) {
            result = new ListNode(list1.val, null);
            list1 = list1.next;
        }
        else {
            result = new ListNode(list2.val, null);
            list2 = list2.next;
        }
        
        // save result head
        ListNode resultHead = result;
        
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                ListNode insert = new ListNode(list1.val);
                result.next = insert;   
                list1 = list1.next;
            }
            else {
                ListNode insert = new ListNode(list2.val);
                result.next = insert;
                list2 = list2.next;
            }
            result = result.next;
        }
        
        if (list1 == null) {
            result.next = list2;
        }
        
        if (list2 == null) {
            result.next = list1;
        }
        
        return resultHead;
            
        }
    }
}