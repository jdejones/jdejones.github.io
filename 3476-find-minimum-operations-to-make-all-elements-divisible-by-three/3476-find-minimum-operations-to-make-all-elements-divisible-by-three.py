class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            plus = 0
            minus = 0
            j = i
            while j % 3 != 0:
                 j += 1
                 plus += 1
            j = 1
            while j % 3 != 0:
                j -= 1
                minus -= 1
            n += min(plus, abs(minus))
        return n