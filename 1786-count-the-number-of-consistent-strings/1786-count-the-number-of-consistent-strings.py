class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        con_strs = 0
        for s in words:
            for i,c in enumerate(s):
                if (i < len(s) - 1) and (c in allowed):
                    continue
                elif (i == len(s) - 1) and (c in allowed):
                    con_strs += 1
                else:
                    break
        return con_strs