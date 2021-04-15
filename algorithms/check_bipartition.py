import ast
from operator import itemgetter
from collections import defaultdict


def check_bipartition(start):
    global IsBipartite
    for u in V[start]:
        if Color[u] == 0:
            Color[u] = 3 - Color[start]
            check_bipartition(u)
        elif Color[u] == Color[start]:
            IsBipartite = False


i = 1
with open("graph1.txt", "r") as f:
    graph1 = list(ast.literal_eval(f.read()))

vCount = max(graph1, key=itemgetter(1))[1] + 1
V = [i for i in range(0, vCount - 1)]
Color = [0] * (vCount + 1)
IsBipartite = True
d = defaultdict(list)
for v, k in graph1:
    d[v].append(k)
    d[k].append(v)
for i in range(1, vCount + 1):
    if Color[i] == 0:
        Color[i] = 1
        check_bipartition(i)
