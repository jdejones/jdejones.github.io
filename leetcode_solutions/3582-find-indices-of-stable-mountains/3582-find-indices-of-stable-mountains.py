class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable = []
        for n in range(1, len(height)):
            if height[n-1] > threshold:
                stable.append(n)
        return stable
