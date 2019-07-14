from collections import deque
# 例えば以下のように
G = [[] for i in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

color = [-1 for i in range(N)]
visits = [False for i in range(N)]
paths = deque()


def Bipartial():
    paths.append(0)
    color[0] = 0
    while paths:
        x = paths.pop()
        visits[x] = True
        for g in G[x]:
            if visits[g] and color[g] == color[x]:
                return False
            elif not visits[g]:
                paths.append(g)
                color[g] = (color[x]+1) % 2
    return True


if Bipartial():
