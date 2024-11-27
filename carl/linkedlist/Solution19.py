# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # cur -> 1 -> 2 -> 3 -> 4 -> 5; n=2 (del 4)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast, slow = dummy, dummy

        # fast -> 3 -> 4 -> 5
        # slow -> 1 -> 2 -> 3 -> 4 -> 5
        while n and fast is not None:
            fast = fast.next
            n = n - 1

        # fast -> None
        # slow -> 4 -> 5
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # slow -> 5
        slow.next = slow.next.next

        return dummy.next

    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     dummy = ListNode(-1, head)
    #     cur = dummy
    #     # list len
    #     len = 0
    #     while cur.next is not None:
    #         len += 1
    #         cur = cur.next
    #     cur = dummy
    #     # cur -> 3 -> 4 -> 5
    #     for _ in range(len - n):
    #         cur = cur.next

    #     # cur -> 3 -> 5
    #     cur.next = cur.next.next
    #     return dummy.next


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    head = ListNode(l[0])
    current = head
    for value in l[1:]:
        current.next = ListNode(value)
        current = current.next

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, 2)

    # Print the resulting linked list
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
