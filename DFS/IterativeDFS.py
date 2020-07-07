#DFS algorithm implemented iteratively.

#CODE:
class Graph:
    graph_dict = {}

    def addEdge(self, u, v):
        if u not in self.graph_dict:
            self.graph_dict[u] = [v]
        else:
            self.graph_dict[u].append(v)


    def DFS(self, node):
        print(self.graph_dict)
        visited = {}
        for i in self.graph_dict:
            visited[i] = False

        stack = [node]
        visited[node] = True
        while stack:
            n = stack.pop(len(stack) - 1)
            for i in self.graph_dict[n]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True

            print(n)


g= Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.addEdge('3', '4')
g.addEdge('4', '3')
g.DFS('1')
