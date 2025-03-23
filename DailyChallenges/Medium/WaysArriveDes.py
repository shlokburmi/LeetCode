#1976. Number of Ways to Arrive at Destination
from math import inf
from typing import List
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        INF = inf
        MOD = 10 ** 9 + 7
        graph = [[INF] * n for _ in range(n)]
        for u, v, time in roads:
            graph[u][v] = time
            graph[v][u] = time
        graph[0][0] = 0
        distance = [INF] * n
        ways = [0] * n
        distance[0] = 0
        ways[0] = 1
        visited = [False] * n
        for _ in range(n):
            current_node = -1
            for i in range(n):
                if not visited[i] and (current_node == -1 or distance[i] < distance[current_node]):
                    current_node = i
            visited[current_node] = True
            for neighbor in range(n):
                if neighbor == current_node:
                    continue
                new_distance = distance[current_node] + graph[current_node][neighbor]
                if distance[neighbor] > new_distance:
                    distance[neighbor] = new_distance
                    ways[neighbor] = ways[current_node]
                elif distance[neighbor] == new_distance:
                    ways[neighbor] += ways[current_node]
        return ways[n - 1] % MOD