class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = [0 for i in nums if i % 2 == 0]
        odd = [1 for i in nums if i % 2 != 0]
        return sorted(even + odd)