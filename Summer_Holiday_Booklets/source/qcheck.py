"""Independent graph checks for network questions."""
import heapq


def dijkstra(edges, s, t):
    adj = {}
    for (u, v), w in edges.items():
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    dist = {s: 0}
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == t:
            return d
        if d > dist.get(u, 1e9):
            continue
        for v, w in adj[u]:
            if d + w < dist.get(v, 1e9):
                dist[v] = d + w
                heapq.heappush(pq, (d + w, v))


def mst(edges):
    parent = {}

    def find(a):
        parent.setdefault(a, a)
        while parent[a] != a:
            a = parent[a]
        return a
    total = 0
    for (u, v), w in sorted(edges.items(), key=lambda kv: kv[1]):
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
            total += w
    return total
