# Solution for geeks for geeks practice question dfs
# Link Of the Question https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

answer = []
def dfs(g, N):
    global answer
    answer = []
    visited = [False] * N
    dfs_helper(g, 0, visited)
    return answer


def dfs_helper(g, node, visited):
    queue = []
    answer.append(node)
    queue.append(node)
    visited[node] = True
    while len(queue) != 0:
        vertex = queue.pop(0)
        for i in g[vertex]:
            if visited[i] == False:
                visited = dfs_helper(g, i, visited)
    return visited