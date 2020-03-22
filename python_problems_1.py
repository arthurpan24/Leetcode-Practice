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

# Problem 2: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Solution: Space: O(n), Time: O(n)
def problem2(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnNode = ListNode(0)
        tailPointer = returnNode
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            sum = val1 + val2 + carry

            carry = (1 if sum >= 10 else 0)
            sum = (sum - 10 if sum >= 10 else sum)

            tailPointer.next = ListNode(sum)
            tailPointer = tailPointer.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return returnNode.next

# Problem 3: Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# Solution: Sliding Window, Space: O(n), Time: O(n)
def problem3(s):
        """
        :type s: str
        :rtype: int
        """
        maximum = i = j = 0
        dict = {}
        while i < len(s) and j < len(s):
            if s[j] not in dict:
                dict[s[j]] = 1
                j += 1
                maximum = max(maximum, j-i)
            else:
                dict.pop(s[i])
                i += 1
        return maximum
