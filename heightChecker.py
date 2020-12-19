"""
Height Checker
Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students that must move in order for all 
students to be standing in non-decreasing order of height.
Notice that when a group of students is selected they can reorder in any 
possible way between themselves and the non selected students remain on their seats.
https://leetcode.com/problems/height-checker/
"""
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        heights_2 = sorted(heights)
        for i in range(0,len(heights)):

            if heights[i] != heights_2[i]:
                count += 1
        return count
