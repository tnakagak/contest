# coding: utf-8
# 部分和問題

# iまででsumを作って、残りi以降を調べる
def dfs(i, sum):
    # n個決め終わったら、今までの和sumがkと等しいかを返す
    if i == n: return sum == k

    # a[i]を使わない場合
    if dfs(i+1, sum): return True

    # a[i]を使う場合
    if dfs(i+1, sum+a[i]): return True

    # a[i]を使う使わないに限らずkが作れないのでFalseを返す
    return False


if __name__ == '__main__':
    # 例1
    n = 4
    a = [1,2,4,7]
    k = 13
    if dfs(0, 0): print "Yes"
    else: print "No"
    
    # 例2
    n = 4
    a = [1,2,4,7]
    k = 15
    if dfs(0, 0): print "Yes"
    else: print "No"
