from itertools import count
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        for i in range(0, len(nums)):
            if i == 0:
                leftSum.append(0)
                rightSum.append(sum(nums[1:]))
            elif i == len(nums)-1:
                rightSum.append(0)
                leftSum.append(sum(nums[:-1]))
            else:
                leftSum.append(sum(nums[:i]))
                rightSum.append(sum(nums[i+1:]))
        answer = [abs(leftSum[i] - rightSum[i]) for i in range(0, len(nums))]
        return answer