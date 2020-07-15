import math
I = math.inf
cost  = [
            [I, I, I, I, I, I, I, I],
            [I, I, 25, I, I, I, 5, I],
            [I, 25, I, 12, I, I, I, 10],
            [I, I, 12, I, 8, I, I, I],
            [I, I, I, 8, I, 16, I, 14],
            [I, I, I, I, 16, I, 20, 18],
            [I, 5, I, I, I, 20, I, I],
            [I, I, 10, I, 14, 18, I, I],
    ]




def prims(cost):
    visited = [I] * (len(cost))
    min = I
    start = I
    end = I
    result = [[0]*len(cost),[0]*len(cost)]
    for i in range(1,len(cost)):
        for j in range(i,len(cost)):
            if cost[i][j] < min:
                min = cost[i][j]
                start = i
                end = j
    result[0][0] = start
    result[1][0] = end
    visited[start] = 0
    visited[end] = 0

    for i in range(1,len(cost)):
        if visited[i] !=0:
            if cost[i][start] < cost[i][end]:
                visited[i] = start
            else:
                visited[i] = end

    for i in range (1,len(cost) -2):
        min = I
        for j in range(1,len(cost)):
            if visited[j]!=0 and cost[j][visited[j]] < min:
                min = cost[j][visited[j]]
                start = j
                end = visited[j]
        result[0][i] = start
        result[1][i] = end
        visited[start] = 0
        for j in range(1,len(cost)):
            if visited[j]!=0 and cost[j][start] < cost[j][visited[j]]:
                visited[j]=start

    total = 0
    for i in range(0,len(cost)-2):
        print(str(result[0][i])+"---"+str(result[1][i])+" : "+str(cost[result[1][i]][result[0][i]]))
        total = total + cost[result[1][i]][result[0][i]]
    print("*"*75)
    print("Total Cost is "+str(total))









prims(cost)
