"""
def fun(s):
  n = len(s)
  num_set = set()
  ans = []
  
  def back(i):
    if i == n:
      # st = '.'.join(s)
      # if st not in num_set:
      ans.append(s)
      # num_set.add(st)
      return

    for j in range(i, n):
      s[i], s[j] = s[j], s[i]
      back(i+1)
      s[i], s[j] = s[j], s[i]
  back(0)
  print(len(ans))
  
fun(["a","b","a","c"])
# input array ={{1,2},{2,3},{0,4},{0,5}},
# query(1,3)->1

parent[1,2,4,5]
parent[6,7,9,10] 

1 ->  2 -> 3 -> 4
  -----------> 4 

6 ->  7 -> 9
  -> 10

  query(2, 10)
"""


class Sol:
  def __init__(self, n):
    self.adj = {x: [] for x in n}
    self.components = {}

    # adj[winner].child.append(loser)

    def input(self, arr):
        for u, v in arr:
            pass
          

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # 1 -> 3  
        # -> 2
    # level[1] = 1
    # level[3] = 2

    # parent 
    # 1 -> 3 
    # 2 -> 3
    # 3 -> 2 
      # -> 1
      # 
      # map[2] = (node, level)

    #   1 -> 3 
        # -> 2
    
    # 3.level = [1]
    # 3.parent = []
    # map[3] = (3, 1)   1 ->  
    #                          3
                        # 2 -> 
    # map[1] = (1, 2)

    # 2 -> 3
    # O(2 * n)

    # def insert(winner, loser):
    #     if not map[loser] and not map[winner] :
    #         map[loser].Node = Graph[loser]
    #         map[winner].Node = Graph[winner]

    #         map[loser].Level = 0
    #         map[winner].Level = 1

    #     if not map[loser] :
    #         map[loser].Node = Graph[loser]
    #         map[loser].Level = map[winner].Level - 1

    #     if not map[winner] :
    #         map[winner].Node = Graph[winner]
    #         map[winner].Level = map[winner].Level + 1

    #     else :
    #         map[winner].Level = map[winner].Level + 1

 
    def insert(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u != parent_v :
            

            

            

            

    
    def query(self, u, v):
        if self.parent[u] != self.parent[v] :
        return u if u > v else v
        else :
        if self.level[u] != self.level[v]:
            return u if self.level[u] > self.level[v] else v
        else:
            return u if u > v else v
        
sol = Sol(6)