class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negs = 0
        poss = 0
        if nums[0] > 0:
            return len(nums)
        elif nums[-1] < 0:
            return (len(nums))
        for i in range(len(nums)):
            if (nums[i] >= 0) and (i > 0) and (nums[i-1] < 0):
                negs += len(nums[:i])
            if (nums[i] > 0) and (nums[i-1] <= 0):
                poss += len(nums[i:])
        return max(negs, poss)
