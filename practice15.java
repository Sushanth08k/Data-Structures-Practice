//Sort List
// Given the head of a linked list, return the list after sorting it in ascending order.
// Input: head = [4,2,1,3]
// Output: [1,2,3,4]

class Solution {
    public ListNode sortList(ListNode head) {
        if (head==null || head.next==null){
            return head;
        }
        ListNode mid=getmid(head);
        ListNode left=sortList(head);
        ListNode right=sortList(mid);
        return merge(left,right);
    }
    ListNode merge(ListNode left,ListNode right){
        ListNode dummyHead=new ListNode(0);
        ListNode tail=dummyHead;
        while(left!=null && right!=null){
            if (left.val<right.val){
                tail.next=left;
                left=left.next;
                
            }else{
                tail.next=right;
                right=right.next;
            }
            tail=tail.next;
        tail.next=(left!=null)?left:right;
        }return dummyHead.next;
    }
    ListNode getmid(ListNode head){
        ListNode slow=head;
        ListNode fast=head;
        ListNode prev = null;
        while (fast != null && fast.next != null){
            prev = slow;
            slow=slow.next;
            fast=fast.next.next;
        }
        if (prev != null) {
            prev.next = null;
        }
        return slow;
    }
}