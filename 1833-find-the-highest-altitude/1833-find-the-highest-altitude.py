class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        highest = 0
        for i in gain:
            alt += i
            if alt > highest:
                highest = alt
        return highest