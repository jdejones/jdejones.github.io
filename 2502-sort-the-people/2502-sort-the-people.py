class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_sorted = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        return [name[0] for name in names_sorted]