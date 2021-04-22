import ast

with open("graph2.txt", "r") as f:
    graph2 = list(ast.literal_eval(f.read()))
n = max([max(graph2[i][1], graph2[i][1]) for i in range(len(graph2))])
A = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if (i, j) in graph2 or (j, i) in graph2:
            A[i][j] = 1


def BiComp(v):
    global i
    num[v] = i
    L[v] = i
    i += 1
    list_v = [j for j in range(n + 1) if A[j][v] == 1]
    for u in list_v:
        if num[u] == 0:
            SE.append((u, v))
            father[u] = v
            BiComp(u)
            L[v] = min(L[v], L[u])
            if L[u] >= num[v]:
                if v != v0:
                    if v not in JPoints:
                        JPoints.append(v)
                else:
                    if len([father[j] for j in range(n + 1) if father[j] == v]) > 1 and v not in JPoints:
                        JPoints.append(v)
                B = []
                B.append(SE[-1])
                while SE[-1] != (u, v):
                    SE.pop()
                    B.append(SE[-1])
                SE.pop()
                Blocks.append(B)
        else:
            if num[u] < num[v] and u != father[v]:
                SE.append((u, v))
                L[v] = min(L[v], num[u])


v0 = 10
i = 1
SE, B, Blocks, JPoints = [], [], [], []
father = [-1 for j in range(n + 1)]
L = [n + 1 for j in range(n + 1)]
num = [0 for j in range(n + 1)]
BiComp(v0)

print(JPoints)
print(Blocks)

# with open("Blocks.txt", "w") as file:
#     print(Blocks, file=file)
# with open("JPoints.txt", "w") as file:
#     print(JPoints, file=file)
