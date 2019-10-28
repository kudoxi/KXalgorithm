class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, strs):
        # write your code here
        a = len(list(strs))
        b = len(set(list(strs)))
        if b < a:
            return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isUnique('abc_____'))