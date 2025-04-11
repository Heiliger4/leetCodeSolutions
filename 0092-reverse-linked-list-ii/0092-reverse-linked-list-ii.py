class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the leftth node
        for _ in range(left - 1):
            prev = prev.next
        
        # Start of the sublist to reverse
        start = prev.next
        then = start.next
        
        # Reverse the sublist
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next

        