# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 3 -> 2 -> 0 -> -4 -> 2(cycle)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            # 1: fast(0) -> -4 -> 2 -> 0 -> -4 -> 2(cycle)
            # 2: fast(2) -> 0 -> -4 -> 2(cycle)
            # 3: fast(-4) -> 2 -> 0 -> -4 -> 2(cycle); fast == slow
            fast = fast.next.next
            # 1: slow(2) -> 0
            # 2: slow(0) -> -4
            # 3: slow(-4) -> 2; slow == fast
            slow = slow.next
            # fast(-4) -> 2 -> 0 -> -4 -> 2(cycle)
            # head(3) -> 2 -> 0 -> -4 -> 2(cycle)
            if fast == slow:
                p1 = head
                p2 = fast
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p2
        return None
