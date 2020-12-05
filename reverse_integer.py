"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment that could only store integers within the 32-bit
signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""
# Reverse Integer Leetcode
# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed = (-1 if x < 0 else 1) * int(str(x)[::-1].replace("-",""))
        if reversed > pow(2,31) - 1 or reversed < -1 * pow(2, 31):
            return 0
        return reversed