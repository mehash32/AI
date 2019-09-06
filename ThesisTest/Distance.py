flowcost = [[0, 90, 689, 194, 165, 494], [668, 0, 1324, 811, 241, 206], [631, 387, 0, 125, 281, 375], [80, 495, 615, 0, 222, 221],
 [276, 204, 1127, 490, 0, 676], [109, 409, 1780, 394, 200, 0], [0, 257, 1632, 330, 117, 285],
 [159, 0, 1309, 297, 803, 404], [98, 82, 0, 271, 222, 383], [110, 404, 1174, 0, 750, 386], [73, 507, 1679, 190, 0, 107],
 [152, 487, 355, 646, 315, 0], [0, 1112, 505, 422, 414, 132], [627, 0, 560, 99, 227, 86], [373, 2007, 0, 235, 384, 205],
 [482, 1638, 262, 0, 233, 129], [223, 1196, 520, 55, 0, 75], [200, 782, 271, 292, 235, 0],
 [0, 1348, 490, 447, 186, 169], [625, 0, 74, 307, 777, 326], [114, 1645, 0, 288, 975, 68], [156, 578, 447, 0, 554, 212],
 [353, 732, 118, 373, 0, 283], [328, 1071, 387, 352, 199, 0], [0, 159, 1103, 218, 297, 95],
 [631, 0, 1618, 95, 253, 109], [552, 213, 0, 432, 397, 141], [418, 122, 797, 0, 108, 495],
 [115, 154, 1610, 425, 0, 158], [167, 214, 2092, 471, 323, 0]]
shiftcost = [898    ,911   , 627    ,538    ,738,977]
fc = flowcost[6:12]
print(len(fc))
print(fc)
x = fc.index([0, 257, 1632, 330, 117, 285])
print(x)

def index_2d(fc, v):
    for i, x in enumerate(fc):
        if v in x:
            return (i, x.index(v))

y = index_2d(fc,257)
print(y)

def distance (fc):
    list1 = []
    for i in range (0, len(fc)):

        a = i*6
        b = a + 6
        f = flowcost[a:b]
        # 6 = departments
        for j in range (0, len(f)):
            list1.append(index_2d(fc, fc[i][j]))
    return list1
xx = distance(fc)
def TotalShiftCost(sequence,shiftCost,N):
    sc  = 0
    T = len(sequence)
    for t in range (1,T):
        X1 = sequence[t-1]
        X2 = sequence[t]
        for j in range (0,N):
            if (X1.index(j+1) != X2.index(j+1) ):
                sc += shiftCost[j]
    return sc
print(xx)
time_period = 5
department = 6
cost =0

seq1 = [[5, 4, 1, 3, 2, 6], [4, 3, 5, 1, 2, 6], [4, 3, 6, 1, 2, 5], [3, 5, 4, 1, 2, 6], [2, 4, 3, 1, 6, 5]]
seq = []
for a in range(0,2):
    seq2 = []
    x = a*3
    y = x+3
    for i in range(x,y):
        seq2.append(seq1[0][i])
    seq.append(seq2)
print("hi", seq)
cost += TotalShiftCost(seq,shiftcost,department)
