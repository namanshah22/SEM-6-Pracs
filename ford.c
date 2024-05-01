#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

// Number of vertices in the graph
#define V 6

// Function to find the maximum flow using Ford-Fulkerson algorithm
int fordFulkerson(int graph[V][V], int source, int sink) {
    int u, v;

    // Create a residual graph and initialize the residual capacities
    int rGraph[V][V]; // Residual graph where rGraph[i][j] indicates residual capacity of edge from i to j
    for (u = 0; u < V; u++)
        for (v = 0; v < V; v++)
            rGraph[u][v] = graph[u][v];

    // Array to store the path from source to sink
    int parent[V];

    // Maximum flow initialized to 0
    int max_flow = 0;

    // Augment the flow while there's a path from source to sink
    while (true) {
        // Find an augmenting path using DFS and store the path in parent[]
        bool visited[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;
        visited[source] = true;
        parent[source] = -1;

        // Create a queue for BFS
        int queue[V];
        int front = 0, rear = 0;
        queue[rear++] = source;

        while (front != rear) {
            int u = queue[front++];
            for (v = 0; v < V; v++) {
                if (!visited[v] && rGraph[u][v] > 0) {
                    parent[v] = u;
                    visited[v] = true;
                    queue[rear++] = v;
                }
            }
        }

        // If we reached the sink, we found an augmenting path
        if (visited[sink]) {
            // Find the minimum residual capacity along the path
            int path_flow = INT_MAX;
            for (v = sink; v != source; v = parent[v]) {
                u = parent[v];
                if (rGraph[u][v] < path_flow)
                    path_flow = rGraph[u][v];
            }

            // Update residual capacities and reverse edges along the path
            for (v = sink; v != source; v = parent[v]) {
                u = parent[v];
                rGraph[u][v] -= path_flow;
                rGraph[v][u] += path_flow;
            }

            // Add path flow to overall flow
            max_flow += path_flow;
        } else {
            // If there's no augmenting path, we are done
            break;
        }
    }

    return max_flow;
}

int main() {
    // Example graph
    int graph[V][V] = {
        {0, 16, 13, 0, 0, 0},
        {0, 0, 10, 12, 0, 0},
        {0, 4, 0, 0, 14, 0},
        {0, 0, 9, 0, 0, 20},
        {0, 0, 0, 7, 0, 4},
        {0, 0, 0, 0, 0, 0}
    };

    int source = 0; // Source vertex
    int sink = 5;   // Sink vertex

    printf("The maximum possible flow is %d\n", fordFulkerson(graph, source, sink));

    return 0;
}
