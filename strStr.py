class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if not target or (target == source):
            return 0
        if not source or len(source) < len(target):
            return -1
        has = -1
        delta = len(source)-len(target)
        for i in range(delta+1):
            strs = ""
            n = i
            for k in range(len(target)):
                strs += source[n]
                n += 1
            if strs == target:
                has = i
                break
        return has