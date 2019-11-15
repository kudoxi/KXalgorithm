class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        C = []
        if A < B:
            C.extend(A)
            C.extend(B)
        else:
            C.extend(B)
            C.extend(A)
        return sorted(C)


if __name__ == "__main__":
    print(Solution().mergeSortedArray([1,2,3,4], [2,4,5,6]))

