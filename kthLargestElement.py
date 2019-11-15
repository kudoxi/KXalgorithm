class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if n > len(nums):
            return False
        nums = sorted(nums, reverse=True)
        return nums[n-1]

if __name__ == "__main__":
    print(Solution().kthLargestElement(6, [9,3,2,4,8]))