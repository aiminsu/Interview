# 推想科技-图像算法岗-现场笔试
'''
输入一个包含‘0-9’，‘+’，‘-’组成的字符串，输出所有数字加减的结果。
'''
def solution(s):
    num = 0
    res = 0
    sign = 1
    for val in s:
        if val.isdigit():
            num = num*10 + sign*int(val)
        elif val == '-':
            res += num
            num = 0
            sign = -1
        elif val == '+':
            res += num
            num = 0
            sign = 1
    res += num
    return res

if __name__ == '__main__':
    s = '-1-2+30'
    print(solution(s))
