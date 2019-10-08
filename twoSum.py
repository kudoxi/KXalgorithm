class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        a = 0
        res = []
        for i in numbers:
            numbers2 = numbers.copy()
            numbers2.remove(i)
            for k in numbers2:
                if target == (k + i):
                    res.append(a)
            a += 1
        return res

if __name__ == "__main__":
    print(Solution().twoSum([15, 2, 7, 11], 9))
    # Solution().getNarcissisticNumbers(1)