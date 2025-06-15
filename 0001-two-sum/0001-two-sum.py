class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            for num2 in nums:
                if (num == num2):
                    if num2 in nums[nums.index(num)+1:]:
                        if num + num2 == target:
                            idx1 = nums.index(num)
                            del nums[nums.index(num)]
                            idx2 = nums.index(num2) + 1
                            return [idx1, idx2]
                elif num + num2 == target:
                    return [nums.index(num), nums.index(num2)]