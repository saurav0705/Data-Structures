import math
I = math.inf
cost  = [ [ 1, 1,  2,  2, 3,  4,  4,  5,  5],
          [ 2, 6,  3,  7, 4,  5,  7,  6,  7],
          [25, 5, 12, 10, 8, 16, 14, 20, 18]
          ];
set = [-1]*8

def union(u,v):
    if set[u] > set[v]:
        set[u]= set[u]+set[v]
        set[v]=u
    else:
        set[v]=set[v]+set[u]
        set[u]=v

def find(u):
    x = u
    while(set[x] > 0):
        x = set[x]
    while(u!=x):
        v=set[u]
        set[u]=x
        u = v
    return x


def krushkals(cost):
    result = []
    index = I
    visited = [False]*len(cost[0])
    for i in range(0,len(cost[0])-1):
        min = I
        start = I
        end = I
        for i in range(0,len(cost[0])):
            if not visited[i] and cost[2][i] < min:
                min = cost[2][i]
                start = cost[0][i]
                end = cost[1][i]
                index = i
        print(min,end=" --> ")
        print(start,end=" , ")
        print(end)
        if(find(start) != find(end)):
            result.append([start,end,min])
            union(find(start),find(end))
        visited[index] = True
    total = 0
    for elem in result:
        total = total +elem[2]
    print(total)






krushkals(cost)