
def removeS(S, x):
    while x in S:
        S.remove(x)

def pointsCover(S) -> list:
    rez = []
    while len(S) != 0:
        Xm = int(min(S))
        rez.append([Xm, Xm + 1])
        removeS(S,Xm)
        removeS(S, Xm + 1)
    return rez
    
if __name__ == '__main__':
    S = [3, 4, 1, 3, 1, 2, 6, 8, 5]
    print(pointsCover(S))

