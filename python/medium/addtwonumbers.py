# PROMPT

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# PROMPT

# Solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        _sum = self.calc_num(l1) + self.calc_num(l2)

        return self.convert_to_list(_sum)

    def calc_num(self, _list):
        multiplier = 1
        num = 0

        while _list is not None:
            num += multiplier * _list.val
            multiplier *= 10
            _list = _list.next

        return num

    def convert_to_list(self, num):
        ret_list = ListNode()

        head = ret_list

        for index, value in enumerate(str(num)[::-1]):
            ret_list.val = int(value)
            if index == len(str(num)) - 1:
                break
            ret_list.next = ListNode()
            ret_list = ret_list.next

        return head
