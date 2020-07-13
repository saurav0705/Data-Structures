# Solution for geeks for geeks practice question bfs
# Link Of the Question https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

def bfs(g, node):
    answer = []
    visited = [False] * node
    queue = []
    answer.append(0)
    visited[0] = True
    queue.append(0)
    while len(queue) != 0:
        vertex = queue.pop(0)
        for elem in g[vertex]:
            if not visited[elem]:
                visited[elem] = True
                answer.append(elem)
                queue.append(elem)

    return answer