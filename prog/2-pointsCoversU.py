
def pointsCoverU(S):
    rez = []
    i = 0
    r = S[i] + 1
    while i < len(S):
        rez.append([S[i], S[i] + 1])
        i += 1
        try:
            while S[i] <= r:
                i += 1
            r = S[i] + 1
        except: pass
    return rez

if __name__ == '__main__':
    S = [3, 4, 1, 3, 9, 2, 6, 8, 5]
    S.sort()
    print(pointsCoverU(S))

