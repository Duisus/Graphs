from operator import itemgetter
from collections import defaultdict


def dfs(v):
    global i
    num[v] = i
    i = i + 1
    for u in d[v]:
        if num[u] == 0:
            T.append((v, u))
            father[u] = v
            dfs(u)
        elif num[u] < num[v] and u != father[v]:
            B.append((v, u))


i = 1
graph = [(0, 1), (0, 2), (0, 5), (0, 6), (0, 7), (0, 9), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (2, 52),
         (3, 6), (3, 7), (3, 8), (4, 5), (4, 51), (5, 9), (6, 7), (6, 8), (7, 8), (9, 51), (9, 52), (10, 17), (10, 21),
         (10, 28), (10, 29), (10, 33), (11, 13), (11, 16), (11, 21), (11, 22), (11, 24), (11, 31), (11, 35), (11, 37),
         (12, 34), (13, 23), (13, 31), (14, 22), (14, 25), (14, 39), (15, 18), (15, 23), (15, 25), (15, 28), (15, 34),
         (15, 36), (15, 39), (16, 39), (17, 27), (17, 29), (17, 34), (17, 36), (18, 29), (18, 34), (18, 35), (18, 38),
         (19, 20), (19, 26), (20, 28), (20, 31), (20, 32), (21, 27), (21, 34), (21, 35), (21, 38), (22, 39), (25, 28),
         (26, 51), (28, 35), (29, 36), (31, 51), (34, 35), (36, 37), (40, 42), (40, 43), (40, 44), (40, 45), (40, 46),
         (40, 47), (41, 42), (41, 43), (41, 44), (41, 45), (41, 47), (41, 48), (41, 49), (42, 44), (42, 45), (42, 46),
         (42, 47), (42, 48), (43, 44), (43, 45), (43, 46), (43, 47), (44, 45), (44, 48), (44, 49), (45, 46), (45, 52),
         (46, 47), (46, 48), (47, 48), (48, 49)]

vCount = max(graph, key=itemgetter(1))[1] + 1
V = [i for i in range(0, vCount - 1)]
num = [0] * vCount
father = [0] * vCount
T = []
B = []
d = defaultdict(list)
for v, k in graph:
    d[v].append(k)
    d[k].append(v)
for v in V:
    if num[v] == 0:
        father[v] = 0
        dfs(v)
