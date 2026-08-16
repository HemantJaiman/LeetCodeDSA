# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        curr = head
        
        while curr.next:
            length += 1
            curr  = curr.next
        
        curr.next = head
        
        k = k % length

        left = head

        for _ in range(length-k-1):
            left = left.next
        
        answer = left.next
        left.next = None

        return answer

        
