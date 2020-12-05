 #Defanging an IP Address Leetcode
 #https://leetcode.com/problems/defanging-an-ip-address/
 class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return ''.join(['[.]' if c == '.' else c for c in address ])