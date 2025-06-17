class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = 0
        for x, i in enumerate(nums):
            for y, j in enumerate(nums):
                if (0 <= x < y) and (nums[x] + nums[y] < target):
                    n+=1
        return n
