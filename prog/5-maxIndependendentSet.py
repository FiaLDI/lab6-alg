def delete(T, r):
    i = 0
    while i != len(T):
        if T[i][1] in r:
            T.pop(i)
            i = i - 1
        i = i + 1

def maximum(T) -> int:
    max = 0
    for i in range(len(T)):
        for j in range(2):
            if T[i][j] > max:
                max = T[i][j]
    return max

def countElemets(T, num) -> int:
    count = 0
    for i in range(len(T)):
        if T[i][0] == num or T[i][1] == num:
            count += 1
    return count

def maxIndependentSet(T) -> list:
    rez = []
    a = maximum(T)
    while len(T) != 0:
        r = []
        for i in range(a, 0, -1):
            t = countElemets(T, i)
            if t == 1:
                r.append(i)
        delete(T, r)
        rez.append(r)
    return rez


if __name__ == "__main__":
    T = [[1, 2], [2, 3], [1, 4], [4, 5], [1, 6], [6, 7], [7, 8], [7, 9], [7, 10], [6, 11]]
    print(maxIndependentSet(T))