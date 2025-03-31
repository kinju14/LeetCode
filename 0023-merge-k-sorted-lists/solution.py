# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeLists(l1, l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                curr.next = ListNode()
                curr = curr.next

                if l1.val < l2.val:
                    curr.val = l1.val
                    l1 = l1.next
                else:
                    curr.val = l2.val
                    l2 = l2.next
            curr.next = l1 or l2
            return dummy.next

        for i in range(1, len(lists)):
            l1 = lists[0]
            l2 = lists[i]

            lists[0] = mergeLists(l1, l2)

        return lists[0]
        
