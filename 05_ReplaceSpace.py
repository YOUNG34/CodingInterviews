'''
*******************************************************************
Copyright(c) 2016, Harry He
All rights reserved.
Distributed under the BSD license.
(See accompanying file LICENSE.txt at
https://github.com/zhedahht/CodingInterviewChinese2/blob/master/LICENSE.txt)
*******************************************************************

==================================================================
《剑指Offer——名企面试官精讲典型编程题》代码
 作者：何海涛
==================================================================

 面试题5：替换空格
 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
 则输出“We%20are%20happy.”。
 
 测试：
 a = Solution()
 a.replaceSpace("we are happy")
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        after_len = 0
        for i in range(len(s)):
            if s[i] == " ":
                after_len += 3
            else:
                after_len += 1
        after_list = [None for i in range(after_len)]
        
        p = after_len - 1
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                after_list[p] = s[i]
                p -= 1
            else:
                after_list[p] = '0'
                after_list[p-1] = '2'
                after_list[p-2]= '%'
                p -= 3
        return("".join(after_list))
