class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum([abs(s.index(c) - t.index(c)) for c in s])