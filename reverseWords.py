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
        for i in range(0, len(arr)):
            arr2.append(arr[len(arr)-1 - i].replace(' ', ''))

        return ' '.join(list(set(arr2))[1:])


if __name__ == "__main__":
    print(Solution().reverseWords('world'))