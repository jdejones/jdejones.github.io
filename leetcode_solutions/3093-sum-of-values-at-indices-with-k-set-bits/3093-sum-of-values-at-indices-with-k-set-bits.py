class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = 0
        for i, _ in enumerate(nums):
            b = bin(i).split('b')[1]
            if sum([int(i) for i in b]) == k:
                n+=_
        return n
