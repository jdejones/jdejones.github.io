class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = 0
        nums_mod = nums
        for i in range(len(nums)-1):
            for j in range(len(nums[i:])-1):
                if (nums[i] == nums[(j+i)+1]) and (i < ((j+i)+1)):
                    n += 1
        return n