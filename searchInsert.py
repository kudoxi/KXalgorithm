import re
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        if target not in A:
            A.append(target)
            A = sorted(A)
        new_str = ', ' + str(A)[1:][:-1] + ','
        a = re.match('.*?, ' + str(target) + ',', new_str)
        if not a:
            return 0
        b = a.group()[1:][:-1].split(",")
        return len(b) - 1


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6,8,9], 7))
