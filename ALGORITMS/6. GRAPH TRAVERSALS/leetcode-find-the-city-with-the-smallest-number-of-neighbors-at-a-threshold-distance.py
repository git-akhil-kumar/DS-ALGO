import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        adj_list = {x: [] for x in range(n)}
        for u,v,cost in edges:
            adj_list[u].append((v, cost))
            adj_list[v].append((u, cost))
        
        def dijikstra(node) :
            minQueue = []
            cities = []
            heapq.heappush(minQueue, (0, node))
            
            distances = [float("inf") for _ in range(n)]
            distances[node] = 0

            while len(minQueue) :
                cur_node, cur_dis = heapq.heappop(minQueue)
                for nei, nei_cost in adj_list[cur_node] :
                    if cur_dis + nei_cost < distances[nei] and cur_dis + nei_cost <= distanceThreshold:
                        distances[nei] = cur_dis + nei_cost
                        cities.append(nei)
                        heapq.heappush(minQueue, (nei, cur_dis + nei_cost))

            return cities
                
        for node in adj_list:
            cities = dijikstra(node)
            print(node, cities)

        return 0

        
sol = Solution()
print(sol.findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))
