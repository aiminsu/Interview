import numpy as np
if __name__ == '__main__':
    N = 10
    res = np.zeros((N, N))
    up, down, left, right = False, False, False, True
    start_row, end_row, start_col, end_col = 0, N-1, 0, N-1
    number = 0
    while (number < N*N):
        if right:
            for _ in range(start_col, end_col+1):
                number += 1
                res[start_row, _] = number
            right = not right
            down = not down
            start_row += 1
        if down:
            for _ in range(start_row, end_row+1):
                number += 1
                res[_, end_col] = number
            down = not down
            left = not left
            end_col -= 1
        if left:
            for _ in range(end_col, start_col-1, -1):
                number += 1
                res[end_row, _] = number
            left = not left
            up = not up
            end_row -= 1
        if up:
            for _ in range(end_row, start_row-1, -1):
                number += 1
                res[_, start_col] = number
            up = not up
            right = not right
            start_col += 1

    print(res)



