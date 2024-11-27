# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        lenA, lenB = self.get_len(headA), self.get_len(headB)

        if lenA > lenB:
            headA = self.move_forward(headA, lenA - lenB)
        else:
            headB = self.move_forward(headB, lenB - lenA)

        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None

    def get_len(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def move_forward(self, head: ListNode, steps: int) -> ListNode:
        for _ in range(steps):
            head = head.next
        return head
