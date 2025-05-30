# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        i = dummy
        j = head
        while n > 0:
            j = j.next
            n -= 1

        while j:
            i = i.next
            j = j.next
        
        i.next = i.next.next

        return dummy.next
