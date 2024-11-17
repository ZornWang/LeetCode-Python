from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        # cur 指向 None 时结束循环，而不是 cur.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == "__main__":
    for i in range(10, 0, -1):
        print(i)
