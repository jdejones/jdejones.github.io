class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(cust) for cust in accounts])
