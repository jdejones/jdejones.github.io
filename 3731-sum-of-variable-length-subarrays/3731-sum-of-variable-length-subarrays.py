class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            start = max(0, i-nums[i])
            sub = nums[start:i+1]
            count += sum(sub)
        return count