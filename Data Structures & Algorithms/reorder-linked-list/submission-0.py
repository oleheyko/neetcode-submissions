# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, dummy
        while right and right.next:
            left = left.next
            right = right.next.next
        
        prev = None
        current = left.next
        left.next = None

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node
        
        l1 = dummy.next
        l2 = prev
        while l1 and l2:
            # Save the next nodes
            temp1 = l1
            l1 = l1.next
            temp2 = l2
            l2 = l2.next
            # Re-wire pointers: temp1 -> temp2 -> l1
            temp1.next = temp2
            temp2.next = l1
            
        


        
        