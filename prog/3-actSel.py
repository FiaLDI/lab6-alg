
def remove(S, Lm, Rm):
    for i in range(len(S)):
        t = [int(k) for k in range(Lm, Rm)]
        try:
            if S[i][0] in t:
                S.pop(i)
        except: pass

def actSel(S) -> list:
    rez = []
    t = 0
    while len(S) != 0:
        min = 111
        for i in range(len(S)):
            if(S[i][1] < min):
                min = S[i][1]
                t = S[i][0]
            if i == len(S)-1:
                rez.append([t, min])
                remove(S, t , min)
    return rez

if __name__ == "__main__":
    S = [[1, 3], [3, 4], [5, 6], [1, 5], [3, 7], [6, 8]]
    print(actSel(S))
