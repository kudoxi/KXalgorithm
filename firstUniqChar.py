class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, strs):
        # Write your code here
        arr = list(strs)
        arr2 = arr.copy()
        res = ''
        for i in arr:
            if i in arr2:
                arr2.remove(i)
                if i in arr2:
                    arr2 = list(''.join(arr2).replace(i, ''))
                else:
                    res = i
                    break
        return res


if __name__ == "__main__":
    print(Solution().firstUniqChar('ahdjksahdkjaskdhaskduqwibmahdjsahdkashdkszaodoadshkasdlksadlspwereratuywuiasdwereratuywuiasdisaiwereratuywuiasdisaiwereratuywuiasdisaiwereratuywuiasdisaiwereratuywuiasdisaiwereratuywuiasdisaiisaid'))
