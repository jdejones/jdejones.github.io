class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(' ')
        n = []
        while len(n) < k:
            n.append(s[len(n)])
        return ' '.join(n)