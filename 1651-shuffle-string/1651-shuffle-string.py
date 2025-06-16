class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shufstr = ''
        for i in range(len(s)):
            index = indices.index(i)
            shufstr += s[index]
        return shufstr