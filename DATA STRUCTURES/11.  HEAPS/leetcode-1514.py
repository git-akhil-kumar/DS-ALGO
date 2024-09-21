from heapq import heappush, heappop
from typing import List


def maxProbability(
    n: int,
    edges: List[List[int]],
    succProb: List[float],
    start_node: int,
    end_node: int,
) -> float:
    adj_list = [[] for _ in range(n)]
    for index, [u, v] in enumerate(edges):
        adj_list[u].append((v, succProb[index]))
        adj_list[v].append((u, succProb[index]))

    max_heap = [(-1.0, start_node)]
    max_prob = [0.0] * n
    max_prob[start_node] = 1.0

    while max_heap:
        curr_node_prob, curr_node = heappop(max_heap)

        curr_node_prob = -curr_node_prob
        if curr_node == end_node:
            return curr_node_prob

        for neigh_node, neigh_prob in adj_list[curr_node]:

            new_prob = neigh_prob * curr_node_prob

            if new_prob > max_prob[neigh_node]:
                max_prob[neigh_node] = new_prob
                heappush(max_heap, (-new_prob, neigh_node))

    return 0.00


ans = maxProbability(
    4,
    [[0, 1], [1, 2], [0, 2], [2, 3], [1, 3]],
    [0.5, 0.5, 0.9999999999, 0.2, 0.9999999999],
    0,
    3,
)
print(ans)

# testcase1 = (
#    maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2)   == 0.25000
# )
# testcase2 = (
#     maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2) == 0.30000
# )

# testcase3 = maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0.00000


# print(testcase1 & testcase2 & testcase3)
