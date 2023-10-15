
def Knapsack(T, W) -> list:
    rez = []
    curW = 0
    T.sort(key=lambda x: (x[1] / x[0]))
    print(T)
    i = len(T) - 1
    while i >= 0:
        curW += T[i][0]
        if curW == W:
            break
        if curW > W:
            t = 0
            for j in range(curW, W, -1):
                t += 1
            coef = 1/(T[i][0] - t)
            w = T[i][0]*coef
            p = T[i][1]*coef
            rez.append([w, p])
        else:
            rez.append(T[i])
        i = i - 1
    return rez

if __name__ == "__main__":
    T = [[2, 14], [4, 20], [3, 18], [5, 30]]
    W = 12
    print(Knapsack(T, W))
