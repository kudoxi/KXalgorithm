class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        res = []
        for i in range(1, n+1):
            a = 'fizz' if i % 3 == 0 else ''
            b = 'buzz' if i % 5 == 0 else ''
            if not a and not b:
                c = str(i)
            else:
                c = a + ' ' + b
                c = c.strip()

            res.append(c)

        return res

if __name__ == "__main__":
    print(Solution().fizzBuzz(15))
