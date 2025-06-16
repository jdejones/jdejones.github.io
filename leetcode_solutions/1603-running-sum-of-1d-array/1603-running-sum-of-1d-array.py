class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        def sumnums(x):
            return sum(x)
        j = []
        for i in range(len(nums)):
            j.append(sumnums(nums[:i+1]))
        return j
