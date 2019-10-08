class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def singleNumber(self, A):
        # write your code here
        if len(A) == 1:
            return A[0]
        numbers2 = A.copy()
        t = list(set(numbers2))
        # print(t)
        for i in t:
            numbers2.remove(i)
            print(numbers2)
            if len(numbers2) > 0 and i not in numbers2:
                return i



if __name__ == "__main__":
    print(Solution().singleNumber([-1]))
    # Solution().twoSum([1,1,2,2,3,4,4])