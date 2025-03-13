from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        # 新的尾巴
        pre = None
        # null 1(cur)->2->3->null
        while cur:
            # null 1(cur)->2(temp)->3->null
            temp = cur.next
            # null<-1(cur) 2(temp)->3->null
            cur.next = pre
            # null<-1(pre) 2(temp)->3->null
            pre = cur
            # null<-1(pre) 2(cur)->3->null
            cur = temp
        return pre
