class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def get_all_subsets(arr):
            subsets = [[]]
            for num in arr:
                new_subsets = [subset + [num] for subset in subsets]
                subsets.extend(new_subsets)
            return subsets
        xors = []
        for i in get_all_subsets(nums):
            xor = 0
            for j in i:
                xor ^= j
            xors.append(xor)
        return sum(xors)
