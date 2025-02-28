# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode()
        dummy = prev
        while l1 or l2 or carry: 
            node = ListNode()
            prev.next = node
            total = 0
            if l1:
                total = l1.val
                l1 = l1.next
            if l2:
                total += l2.val 
                l2 = l2.next

            total += carry
            carry = total // 10
            total = total % 10
            node.val = total
            prev = node
            
        prev.next = None    
        return dummy.next
