class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums = list(sorted(nums))
        return [num for i, num in enumerate(nums) if num == nums[i - 1]]
