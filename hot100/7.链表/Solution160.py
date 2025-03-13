from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        l_A, l_B = self.get_len(headA), self.get_len(headB)

        if l_A > l_B:
            headA = self.move_forward(headA, l_A - l_B)
        else:
            headB = self.move_forward(headB, l_B - l_A)

        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None

    def get_len(self, head: ListNode) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l

    def move_forward(self, head: ListNode, steps: int) -> ListNode:
        for _ in range(steps):
            head = head.next
        return head
