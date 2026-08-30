class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.countOnes(i))
        return res

    def countOnes(self, n):
        count = 0
        for i in range(32):
            if n & 1:
                count += 1
            n >>= 1
        return count
        