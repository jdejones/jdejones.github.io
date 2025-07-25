class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [nums[_]|nums[_+1] for _ in range(len(nums)-1)]