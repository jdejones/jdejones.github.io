class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        pos = ['type', 'color', 'name']
        count = 0
        for i in items:
            if i[pos.index(ruleKey)] == ruleValue:
                count+=1
        return count
