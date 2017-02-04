'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


class ListNode(object):
    '''Definition for singly-linked list.'''
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remainder = 0
        root = n = ListNode(0)
        while l1 or l2 or remainder:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            remainder, val = divmod(v1 + v2 + remainder, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    expected = [7, 0, 8]
    result_list = []
    result_linked_list = s.add_two_numbers(l1, l2)

    while result_linked_list:
        result_list.append(result_linked_list.val)
        result_linked_list = result_linked_list.next

    assert expected == result_list
