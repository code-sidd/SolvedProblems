"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        r_count = 0
        l_count = 0
        for i in s:
            if i == 'R':
                r_count+=1
            else:
                l_count += 1
            if r_count == l_count and r_count != 0:
                res += 1
                r_count = l_count = 0
        return res
