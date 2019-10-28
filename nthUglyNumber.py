import time
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    # 只算丑数的部分，可以把每一个丑数看成
    # 1,
    # 1*2,1*3,1*5,
    # 2*2,2*3,2*5,
    # ...
    # 但是这些数没有按照顺序排列，我们需要按照顺序加入到数组内
    def nthUglyNumber(self, n):
        # write your code here
        if n == 0:
            return 0
        arr = [1]
        k2, k3, k5 = 0, 0, 0
        minest = 1
        while len(arr) < n:
            a2, a3, a5 = arr[k2]*2, arr[k3]*3, arr[k5]*5
            minest = min(a2, a3, a5)
            arr.append(minest)
            if minest == a2:
                k2 += 1
            if minest == a3:
                k3 += 1
            if minest == a5:
                k5 += 1

        return minest
    # 暴力算法
        # a = 0
        # count = 0
        # while True:
        #     a += 1
        #     if self.is_ugly(a):
        #         count += 1
        #         if count == n:
        #             break
        # return a

    # def is_ugly(self, number):
        # number = self.devide(number, 2)
        # number = self.devide(number, 5)
        # number = self.devide(number, 3)
        #
        # if number == 1:
        #     return True
        # number2 = number
        # while True:
        #     if number2 % 2 != 0:
        #         break
        #     number2 /= 2
        # while True:
        #     if number2 % 5 != 0:
        #         break
        #     number2 /= 5
        # while True:
        #     if number2 % 3 != 0:
        #         break
        #     number2 /= 3
        # if number2 == 1:
        #     return True

    # def devide(self, number, who):
    #     while True:
    #         if number % who != 0:
    #             return number
    #         number /= who


if __name__ == "__main__":
    a = time.time()
    print(Solution().nthUglyNumber(1000))
    print(time.time() - a) #2.5275378227233887
    # Solution().rotateString("abcdefg", 3)