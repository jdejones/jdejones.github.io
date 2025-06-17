import string
class Solution:
    def reverseDegree(self, s: str) -> int:
        indexed = dict(zip(string.ascii_lowercase, [i for i in range(1, 27)][::-1]))
        n=0
        for h,i in enumerate(s):
            n += (indexed[i] * (h + 1))
        return n