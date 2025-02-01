def bfs(graph, start_node):
    queue = [start_node]
    visited = [start_node]

    while queue:
        current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)