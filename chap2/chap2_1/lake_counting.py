# coding: utf-8
import sys

# Lake Counting
def lake_counting(field):

    lake_count = 0

    # 現在位置(x, y)
    def dfs(x, y):
        # 今いるところを.に置き換える
        field[x][y] = '.'

        # 移動する8方向をループ
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # x方向にdx, y方向にdyだけ移動した場所を(nx, ny)とする
                nx = x + dx
                ny = y + dy

                # nxとnyが庭の範囲内かどうかとfield[nx][ny]が水たまりかどうかを判定
                if (0 <= nx < N and 0 <= ny < M and field[nx][ny] == 'W'):
                    dfs(nx, ny)

    for i in range(0,N):
        for j in range(0,M):
            if field[i][j] == 'W':
                # Wが残っているならそこから始める
                dfs(i, j)
                lake_count += 1

    return lake_count

if __name__ == '__main__':
    N = int(raw_input())
    M = int(raw_input())
    
    field = [[0 for i in range(N)] for j in range(M)]
    for i in range(N):
        field[i] = list(raw_input())

    print lake_counting(field)

