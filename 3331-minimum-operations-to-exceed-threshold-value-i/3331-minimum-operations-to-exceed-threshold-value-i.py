class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        while min(nums) < k:
            nums.remove(nums[nums.index(min(nums))])
            ops+=1
        return ops