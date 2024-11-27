# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # cur -> 1 -> 2 -> 3 -> 4
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next is not None and cur.next.next is not None:
            # save 1
            tmp1 = cur.next
            # save 3
            tmp2 = cur.next.next.next

            # cur -> 2
            cur.next = cur.next.next
            # 2 -> 1
            cur.next.next = tmp1
            # 1 -> 3
            cur.next.next.next = tmp2

            # cur -> 2 -> 1 -> 3
            # cur >> 1
            cur = cur.next.next
        result = dummy.next
        return result
