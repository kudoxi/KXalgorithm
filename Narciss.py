# 水仙花数
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """

    def getNarcissisticNumbers(self, n):
        # write your code here
        res = []
        m = self.ling(n + 1, 1) + 1
        print(m)

        for i in range(0, m):
            temp = i
            sum = 0
            a = len(str(i))
            while temp:
                sum += (temp % 10) ** a
                temp //= 10
            if sum == i and len(str(i)) == n and n != 2:
                res.append(i)
        return res

    def ling(self, n, a):
        l = n - 1
        l2 = a
        for i in range(l):
            l2 = l2 * 10

        return l2



if __name__ == "__main__":
    print(Solution().getNarcissisticNumbers(3))
    # Solution().getNarcissisticNumbers(1)

