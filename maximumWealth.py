#https://leetcode.com/problems/richest-customer-wealth/
# Richest Customer Wealth

def maximumWealth(accounts):
    return max([sum(i) for i in accounts])