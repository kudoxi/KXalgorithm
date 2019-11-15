import re
import time
class Solution:
    """
    @param s: the article
    @return: the number of letters that are illegal
    """
    # def count(self, s):
    #     # Write your code here.
    #     arr = s.split(".")
    #     error = 0
    #     for i in arr:
    #         if i:
    #             arr2 = i.split(" ")
    #             count = 0
    #             for k in arr2:
    #                 if k:
    #                     if count == 0:
    #                         res = re.match('^[A-Z][a-z]+$', k)
    #                         count += 1
    #                         if not res:
    #                             error += 1
    #                     else:
    #                         res = re.match('^[\s]*[a-z]+[,]*[\s]*$', k)
    #
    #                         if not res:
    #                             for m in list(k):
    #                                 if m:
    #                                     res2 = re.match('^[A-Z]*$', m)
    #                                     print(m, res2)
    #                                     if res2:
    #                                         error += 1
    #
    #     return error
    def count(self, s):
        arr = s.split(".")
        error = 0
        for i in arr:
            if i:
                arr2 = i.split(" ")
                n = 0
                for k in arr2:
                    if k:
                        if n == 0:
                            # 首字母是否大写
                            res = re.match('^[A-Z][a-z]+$', k)
                            if not res:
                                print(k)
                                error += 1
                        else:
                            # 字中是否有大写
                            k = k[1:]
                            res = re.findall('[A-Z]', k)
                            if res:
                                print(k)
                                error += len(res)
                        n += 1
                        # print(k)
        return error


if __name__ == "__main__":
    time.clock()
    a = Solution().count(' This won iz correkt. It has, No Mistakes et Oll. But there are two BIG mistakes in this sentence. and here is one more.')
    print(a)