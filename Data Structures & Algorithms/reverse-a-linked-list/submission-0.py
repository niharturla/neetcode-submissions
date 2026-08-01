# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      

        # keep track of right node and state of right
        # curr = head, node=curr->right
        # while we have a node
        # node->next=curr
        # curr = node
        # node=node->right

        prev=None
        curr=head

        while curr:
            nxt=curr.next # save next node
            curr.next=prev # reverse pointer
            prev=curr
            curr=nxt
        return prev



            
        

