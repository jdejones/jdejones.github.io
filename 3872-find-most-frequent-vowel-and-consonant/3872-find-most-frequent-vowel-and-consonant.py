class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        c = {}
        for l in s:
            if l in v:
                v[l] += 1
            else:
                if l in c:
                    c[l] += 1
                    continue
                c[l] = 1

        v_max = sorted(v.items(), key=lambda x: x[1])[-1][-1]
        if len(c) > 0:
            c_max = sorted(c.items(), key=lambda x: x[1])[-1][-1]
        else:
            c_max = 0
        return v_max + c_max