import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pat = re.compile('\w')
        s = ''.join([i for i in s if pat.match(i) and i != '_']).lower()
        if s == s[::-1]:
            return True
        return False
        