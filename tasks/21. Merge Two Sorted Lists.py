"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'

    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next


class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        lst = []
        while list1:
            lst.append(list1.val)
            list1 = list1.next

        while list2:
            lst.append(list2.val)
            list2 = list2.next

        lst.sort()
        lst.reverse()

        last_member = None
        for i in lst:
            temp = ListNode(i, last_member)
            last_member = temp

        return last_member


assert Solution().mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4, None))),
    ListNode(1, ListNode(3, ListNode(4, None)))
) == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None))))))

assert Solution().mergeTwoLists(
    ListNode(), ListNode()
) == ListNode(0, ListNode(0, None))

assert Solution().mergeTwoLists(
    ListNode(), ListNode(0, None)
) == ListNode(0, ListNode(0,None))
