from collections import deque

V = 6

def bfs(rGraph, s, t, parent):
    visited = [False] * V
    q = deque()
    q.append(s)
    visited[s] = True
    parent[s] = -1

    while q:
        u = q.popleft()
        for v in range(V):
            if not visited[v] and rGraph[u][v] > 0:
                if v == t:
                    parent[v] = u
                    return True
                q.append(v)
                parent[v] = u
                visited[v] = True
    return False

def fordFulkerson(graph, s, t):
    rGraph = [row[:] for row in graph]
    parent = [-1] * V
    max_flow = 0

    while bfs(rGraph, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, rGraph[u][v])
            v = parent[v]

        v = t
        while v != s:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

print("The maximum possible flow is", fordFulkerson(graph, 0, 5))
