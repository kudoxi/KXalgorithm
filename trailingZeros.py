import math
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        i = 5
        count = 0
        while n / i >= 1:
            count += math.floor(n / i)
            i *= 5
        return count


if __name__ == "__main__":
    print(Solution().trailingZeros(105))# 250292920