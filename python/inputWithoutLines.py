# 行数が指定されていないときは、こんな感じでやるしかない
# Pycharmでは実行できないことに注意。HackerRankでは動作した
Input = []
while True:
    try:
        i = list(map(str, input().split()))
        Input += i
    except EOFError:
        break
