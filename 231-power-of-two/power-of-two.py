class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return True if n == 1 or math.log2(n) % 1 == 0 else False
        return False if n <= 0 else n == 1 or math.log2(n) % 1 == 0