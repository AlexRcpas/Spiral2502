#!python3

import copy

def convLine(s, m):
    convspam = ''
    for i in range(s-1):
        convspam += str(m[i]).center(len(str(s*s))) + ' '
    convspam += str(m[-1]).center(len(str(s*s)))
    return convspam

def newMt(mxs):
    spiralmx = []
    for x in range(mxs):
        spiralmx.append([])
        for y in range(mxs):
            spiralmx[x].append(0)
    return spiralmx

def spiralMx(mxs):
    mx0 = newMt(mxs)
    spmt = copy.deepcopy(mx0)
    flag = 1
    t = 0
    while flag <= mxs * mxs:
        for cl in range(t, mxs-t):
            spmt[t][cl] = flag
            flag += 1
        for rw in range(t+1, mxs-t):
            spmt[rw][mxs-1-t] = flag
            flag += 1
        for cl in range(mxs-2-t, t-1, -1):
            spmt[mxs-1-t][cl] = flag
            flag += 1
        for rw in range(mxs-2-t, t, -1):
            spmt[rw][t] = flag
            flag += 1
        t += 1
    return spmt

while True:
    print("Tell me the size of the matrix:")
    mxs = int(input())
    if mxs == 0:
        break
    else:
        spmx = spiralMx(mxs)

        for i in range(mxs):
            cvdmx = convLine(mxs, spmx[i])
            print(cvdmx)
        print("\nYou can break out by enter the number '0'.")