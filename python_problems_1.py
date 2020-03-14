from common_classes.py import *

# Problem 1: Two Sum
# Given an array of integers, return indicies of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Solution: One-pass Hash Table, Space: O(n), Time: O(n)
def problem1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i, x in enumerate(nums):
        if target-x not in dict:
            dict[x] = i
        else:
            print("indexes found: " + str(i) + ", " + str(dict.get(target-x)))
    return("not found")
problem1([2, 7, 11, 15],9)

# Problem 2: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
def problem2(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
problem2()
