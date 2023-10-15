
def actSelU(S) -> list:
    S.sort(key=lambda x: x[1])
    rez = [S[0]]
    added = [i for i in range(S[0][0], S[0][1] + 1)]
    for i in range(1, len(S)):
        Cur = [r for r in range(S[i][0], S[i][1] + 1)]
        l = 0
        try:
            for l in range(len(added)):
                if added[l] not in Cur:
                    rez.append(S[i])
                    added = [y for y in range(S[i][0], S[i][1] + 1)]
        except: l = len(added)

    return rez


if __name__ == "__main__":
    S = [[1, 3], [3, 4], [5, 6], [1, 5], [3, 7], [6, 8]]
    print(actSelU(S))
