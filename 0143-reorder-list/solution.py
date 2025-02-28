# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        prev = None
        curr = s.next
        s.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        h2 = prev
        h1 = head

        while h2:
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            h2.next = temp1
            h1 = temp1
            h2 = temp2
            

    

