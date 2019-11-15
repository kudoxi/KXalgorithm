import re
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        # 判断是否有重复
        origin_num = len(nums)
        new_nums = list(set(nums))
        now_num = len(new_nums)
        if origin_num == now_num:
            return nums

        delta = origin_num - now_num

        for i in range(delta):
            new_nums.append("?")
            
        return new_nums

if __name__ == "__main__":
    print(Solution().deduplication([1,2,3,4,4,1]))
