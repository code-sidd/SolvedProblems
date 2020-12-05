#Kids With the Greatest Number of Candies Leetcode
#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if all(val+extraCandies>=elem for elem in candies) else False  for val in candies ]
