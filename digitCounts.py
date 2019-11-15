import re
class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        k = str(k)
        count = 0
        for i in range(n+1):
            res = re.findall(k, str(i))
            count += len(res)

        return count

if __name__ == "__main__":
    print(Solution().digitCounts(1, 12))