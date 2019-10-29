import re
class Solution:
    """
    @param str: The identifier need to be judged.
    @return: Return if str is a legal identifier.
    """
    def isLegalIdentifier(self, strs):
        # Write your code here.
        if not strs or isinstance(strs, int):
            return False
        res = re.match('^[a-zA-Z_][A-Za-z0-9_]+$', strs)
        if res:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isLegalIdentifier('LintCode'))

