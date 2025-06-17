class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i,j in enumerate(encoded):
            arr.append(arr[i]^encoded[i])
        return arr
