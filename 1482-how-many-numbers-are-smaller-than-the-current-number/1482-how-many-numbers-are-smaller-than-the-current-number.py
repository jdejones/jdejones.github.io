class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        nums_sorted = sorted(nums)
        for i in nums:
            arr.append(len(nums_sorted[:nums_sorted.index(i)]))
        return arr
