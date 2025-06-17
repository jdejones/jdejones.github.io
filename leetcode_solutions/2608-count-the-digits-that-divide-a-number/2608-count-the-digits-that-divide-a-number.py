class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(char) for char in str(num)]
        n=0
        for i in digits:
            if num % i == 0:
                n+=1
        return n
