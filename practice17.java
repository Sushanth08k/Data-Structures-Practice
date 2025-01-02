//92 - Reverse Linked List 2
// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        for(int i=1;i<left;i++){
            prev=prev.next;
        }
        ListNode cur=prev.next;
        for(int i=0;i<right-left;i++){
            ListNode temp=cur.next;
            cur.next=temp.next;
            temp.next=prev.next;
            prev.next=temp;
        }return dummy.next;
    }
}