class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = 'aeiou'
        return ''.join([_ for _ in s if _ not in vowels])
