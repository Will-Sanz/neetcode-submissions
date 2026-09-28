class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(str(digit) for digit in digits))
        number += 1
        number = str(number)
        res = []
        for c in number:
            res.append(c)
        return res