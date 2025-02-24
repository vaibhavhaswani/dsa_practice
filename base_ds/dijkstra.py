class WeightedGraph:
    def __init__(self):
        self.graph={}
    
    def add_edge(self,u,v,weight):
        if u not in self.graph:
            self.graph[u]=list()
        if v not in self.graph:
            self.graph[v]=list()
        self.graph[u].append((v,weight))
        
    def dijkstra(self,start):
        pq=[(0,start)] # weight,node
        distances={node:float('inf') for node in self.graph}
        distances[start]=0
        
        while pq:
            curr_dist,node=pq.pop(0)
            if curr_dist>distances[node]:
                continue
            for nb,weight in self.graph[node]:
                new_dist=weight+curr_dist
                if new_dist<distances[nb]:
                    distances[nb]=new_dist
                    pq.append((new_dist,nb))
                    pq.sort(key=lambda x:x[0])
        
        return distances
    
g = WeightedGraph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

source = 0
shortest_paths = g.dijkstra(source)
print(f"Shortest distances from node {source}: {shortest_paths}")