
import heapq


def hotel(arrive, depart, available_rooms):
    n = len(arrive)
    arrivals = [(arrive[i], depart[i]) for i in range(n)]
    del arrive 
    del depart
    arrivals.sort()

    min_heap = []

    for start, end in arrivals :
        if min_heap and min_heap[0] < start :
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, end)

        if len(min_heap) > available_rooms :
            return False

            
    return True

print(hotel([ 5, 6, 20, 5, 12, 13, 13, 17, 13, 10, 12, 8, 15 ], [ 7, 8, 35, 13, 30, 20, 26, 22, 15, 13, 17, 21, 32 ], 13))
    
#           3 -- 4
#      2 -- 3
# 1 -- 2