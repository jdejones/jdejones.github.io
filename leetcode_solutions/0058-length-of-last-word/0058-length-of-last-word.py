class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([item for item in s.split(' ') if '' != item][-1])
