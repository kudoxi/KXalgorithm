class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        array2 = sorted(array, key=lambda x:(-x[1], x[0]))
        return array2


if __name__ == "__main__":
    print(Solution().multiSort([[2,50],[1,50],[3,100]]))