class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        arr = s.split(" ")
        if len(arr) == 1:
            return s
        arr2 = []
        for i in range(len(arr)):
            strs = arr[len(arr)-1 - i]
            if strs:
                arr2.append(strs.replace(' ', ''))
        return ' '.join(arr2)


if __name__ == "__main__":
    print(Solution().reverseWords('row'))