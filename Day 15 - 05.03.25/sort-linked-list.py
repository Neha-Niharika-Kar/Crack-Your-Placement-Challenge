# LINKED LIST - Medium

# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        # Step 1: Find middle node
        mid = self.getMiddle(head)
        right_head = mid.next
        mid.next = None  
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        # Step 3: Merge sorted halves
        return self.merge(left, right)

    def getMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow  
    
    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2 
        return dummy.next  
