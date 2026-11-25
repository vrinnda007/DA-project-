from collections import deque
from time import perf_counter

social_network = {
    "Alice": ["Bob", "Charlie", "David"],
    "Bob": ["Alice", "Emma", "Frank"],
    "Charlie": ["Alice", "David", "Grace"],
    "David": ["Alice", "Charlie", "Harry"],
    "Emma": ["Bob", "Frank"],
    "Frank": ["Bob", "Emma", "Ivy"],
    "Grace": ["Charlie", "John"],
    "Harry": ["David", "John"],
    "Ivy": ["Frank"],
    "John": ["Grace", "Harry"],
    "Kevin": []
}

def bfs(graph, start):
    if start not in graph:
        return []
    visited, queue, order = {start}, deque([start]), []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(graph, start):
    if start not in graph:
        return []
    visited, stack, order = set(), [start], []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    return order

def shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return None
    queue, parent = deque([start]), {start: None}
    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    if end not in parent:
        return None
    path, current = [], end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    edges = list(zip(path, path[1:]))
    return {"vertices": path, "edges": edges,
            "total_vertices": len(path), "total_edges": len(edges)}

def mutual_friends(graph, user1, user2):
    if user1 not in graph or user2 not in graph:
        return []
    return sorted(set(graph[user1]) & set(graph[user2]))

def performance_comparison():
    results = []
    for size in (10, 100, 500):
        graph = {str(i): ([str(i-1)] if i > 0 else []) +
                 ([str(i+1)] if i < size-1 else []) for i in range(size)}
        start = perf_counter()
        bfs(graph, "0")
        results.append({"nodes": size,
                        "time": round((perf_counter() - start) * 1000, 4)})
    return results
