class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        a = 0
        for i in range(1, n+2):
            if self.is_ugly(i):
                a += 1
                if n == a:
                    return i


    def is_ugly(self, number):
        number = self.devide(number, 2)
        number = self.devide(number, 5)
        number = self.devide(number, 3)
        if number == 1:
            return True
        else:
            return False

    def devide(self, number, who):
        temp = 1
        while temp:
            if number % who != 0:
                temp = 0
            else:
                number /= who

        return number

if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
    # Solution().rotateString("abcdefg", 3)