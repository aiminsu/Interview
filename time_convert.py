'''
2018腾讯算法校招笔试题
时制转换
输入: 10:30:45PM
输出：22:30:45
注意: 12:00:00AM-00:00:00

'''
import sys
if __name__ == "__main__":
    # 读取第一行
    line = sys.stdin.readline().strip()
    if line.endswith('AM'):
        line = line.replace('AM','')
        time = list(map(int, line.split(':')))
        if time[0] == 12:
            time[0] = 0
    elif line.endswith('PM'):
        line = line.replace('PM','')
        time = list(map(int, line.split(':')))
        if time[0] != 12:
            time[0] = time[0]+12

    time = [str(t).zfill(2) for t in time]
    print(':'.join(time))
