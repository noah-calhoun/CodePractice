from collections import deque

def shortestChain(graph, start, target):
    if start == target:
        return 0
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for next in graph.get(node, []):
            if next == target:
                return dist + 1
            if next not in visited:
                visited.add(next)
                queue.append((next, dist + 1))

    return -1





if __name__ == '__main__':
    graph = {
    "A": ["B","C"],
    "B": ["D"],
    "C": ["D","E"],
    "D": ["F"],
    "E": [],
    "F": []
    }
    print(shortestChain(graph, "A", "F"))