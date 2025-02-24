class Graph:
    def __init__(self,directed=False):
        self.graph={}
        self.directed=directed

    # directed graph has directions and nodes are not repeated in the set, hence in x --> y , y will be saved in set of x not viseversa
    # undirected graph has no directions so nodes x and y , will both be in sets of each other
    def add_edge(self,x,y):
        if x not in self.graph:
            self.graph[x]=[] #adding key for the edge node x it does't exist
        if y not in self.graph:
            self.graph[y]=[] #adding key for the edge node y it does't exist
            
        self.graph[x].append(y) #registering node with another node to create and edge
        
        if not self.directed: #if undirected , we'll register bidirectionally
            self.graph[y].append(x)
    
    def show_graph(self):
        for node,vertices in self.graph.items():
            print(f"Node {node} --> {vertices}")
            
            
    def dfs_traverse(self,node,visited=None):
        if visited is None:
            visited=set()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for neighbour in self.graph.get(node,[]):
                self.dfs_traverse(neighbour,visited)
                
    def bfs_traverse(self,node):
        visited=set()
        queue=[node]
        while queue:
            node=queue.pop(0)
            if node not in visited:
                print(node,end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node,[]))

        
        
        


if __name__ == "__main__":
    graph=Graph()
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,0)
    graph.show_graph()
    print("DFS Traverse:")
    graph.dfs_traverse(0)
    print()
    print("BFS Traverse:")
    graph.bfs_traverse(0)
    print()