N, W = map(int, input().split())
VW = [list(map(int, input().split())) for _ in range(N)]
VW_w = sorted(VW, key=lambda x: x[0])


def Case1():
    import bisect
    M = N // 2
    res1 = []
    for i in range(2 ** M):
        v = w = 0
        for j in range(M):
            if i & (1 << j):
                continue
            vj, wj = VW[j]
            v += vj
            w += wj
        res1.append((w, v))

    res2 = []
    for i in range(2 ** (N - M)):
        v = w = 0
        for j in range(N - M):
            if i & (1 << j):
                continue
            vj, wj = VW[j + M]
            v += vj
            w += wj
        res2.append((w, v))
    res2.sort()

    optv = [0]
    for w, v in res2:
        optv.append(max(optv[-1], v))
    ans = 0
    for w, v in res1:
        if w > W:
            continue
        i = bisect.bisect(res2, (W - w, float('inf')))
        ans = max(ans, v + optv[i])
    print(ans)


def Case2():
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j < VW[i][1]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-VW[i][1]]+VW[i][0])
    print(dp[-1][-1])


def Case3(VW):
    dp = {0: 0}
    for i in range(N):
        for j in sorted(dp.keys(), reverse=True):
            w, v = VW[i][1], VW[i][0]
            nw = dp[j] + w
            nv = j + v
            if nw <= W:
                if nv in dp:
                    if nw < dp[nv]:
                        dp[nv] = nw
                else:
                    dp[nv] = nw
    print(max(dp.keys()))
