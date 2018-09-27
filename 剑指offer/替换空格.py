'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        oldLen = len(s)
        spaceNum = s.count(' ')
        newLen = oldLen + spaceNum*(3-1)
        # construct a new string, append 0 behind
        s += '0'*(spaceNum*2)
        j = newLen-1 # new string pointer
        for i in range(oldLen-1, -1, -1):
            if s[i] == ' ':
                s[j-2:j+1]='%20'
                j -= 3
            else:
                s[j] = s[i]
                j -= 1
        return ''.join(s)

if __name__ == '__main__':
    s = 'we are happy'
    print(Solution().replaceSpace(s))
