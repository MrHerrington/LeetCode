"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        lst1 = []
        lst2 = []

        while l1:
            lst1.append(l1.val)
            l1 = l1.next

        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        for lst in lst1, lst2:
            lst.reverse()

        lst = int(''.join(map(str, lst1))) + int(''.join(map(str, lst2)))
        final_lst = []
        final_lst.extend(str(lst))
        lst = list(map(int, final_lst))

        last_member = None
        for i in lst:
            temp = ListNode(i, last_member)
            last_member = temp

        return last_member


assert Solution().addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3, None))),
    ListNode(5, ListNode(6, ListNode(4, None)))
) == ListNode(7, ListNode(0, ListNode(8, None)))

assert Solution().addTwoNumbers(
    ListNode(0, None), ListNode(0, None)
) == ListNode(0, None)

assert Solution().addTwoNumbers(
    ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))))),
    ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
) == ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1, None))))))))
