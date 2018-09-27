'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        numRows, numCols = len(array), len(array[0])
        row, col = numRows-1, 0
        while(row>=0 and col<=numCols-1):
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                row -= 1
                continue
            elif array[row][col] < target:
                col += 1
                continue
        return False

if __name__ == '__main__':
    array = [[1,2,3],[4,5,6],[7,8,9]]
    target = 5
    print(Solution().Find(target, array))
