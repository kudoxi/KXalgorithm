class Solution:
    """
    @param str: the str
    @return: the sum that the letter appears the most
    """
    def mostFrequentlyAppearingLetters(self, strs):
        # Write your code here.
        if not strs:
            return 0
        res_dict = {}
        arr = list(strs)
        for i in arr:
            if i in res_dict:
                res_dict[i] += 1
            else:
                res_dict[i] = 1

        sorted(res_dict.items(), key=lambda item:item[1])
        return list(res_dict.values())[0]

if __name__ == "__main__":
    print(Solution().mostFrequentlyAppearingLetters('ABCabcA'))