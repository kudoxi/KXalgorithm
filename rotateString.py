class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if isinstance(s, list):
            s = ''.join(s)
        for i in range(1, offset+1):
            s = s[-1] + s[:-1]

        return s

if __name__ == "__main__":
    print(Solution().rotateString("abcdefg", 3))
    # Solution().rotateString("abcdefg", 3)