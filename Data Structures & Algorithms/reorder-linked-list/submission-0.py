# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1 = head
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        current = slow.next
        slow.next = None
        previous = None
        
        while current:
            current_next = current.next
            current.next = previous
            previous = current
            current = current_next
        
        list2 = previous

        while list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
        