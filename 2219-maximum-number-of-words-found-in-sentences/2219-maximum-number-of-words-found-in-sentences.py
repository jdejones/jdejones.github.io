class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return len(list(sorted([item.split(' ') for item in sentences], key=len)[-1]))