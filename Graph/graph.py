increment = lambda num: num+1
class Graph_Adjancy_List:
    adjancy_list = {}
    nodes = 0
    def __init__(self,nodes):
        self.nodes = nodes
        for i in range(0,nodes):
            self.adjancy_list[i] = []

    def check_invalid(self,vertex_1,vertex_2):
        if vertex_1 < 0 or vertex_2 < 0 or vertex_2 > self.nodes or vertex_1 >self.nodes:
            print("invalid node")
            return True
        return False

    def insert(self,vertex_1,vertex_2):
        if not self.check_invalid(vertex_1, vertex_2):
            self.adjancy_list[vertex_1].append(vertex_2)
            self.adjancy_list[vertex_2].append(vertex_1)

    def print(self):
        for i in range(0,self.nodes):
            # data = list(map(increment,self.adjancy_list[i]))
            print(str(i)+" --> "+str(self.adjancy_list[i]))

    def delete(self,vertex_1,vertex_2):
        if not self.check_invalid(vertex_1,vertex_2):
            if vertex_2-1 in self.adjancy_list[vertex_1]:
                self.adjancy_list[vertex_1].remove(vertex_2)
                self.adjancy_list[vertex_2].remove(vertex_1)
            else:
                print("No Connection Exist")

    def bfs(self,node):
        visited = [False]*self.nodes
        queue = []
        print(node,end="")
        visited[node] = True
        queue.append(node)
        while len(queue) !=0:
            vertex =  queue.pop(0)
            for elem in self.adjancy_list[vertex]:
                if not visited[elem]:
                    visited[elem] = True
                    print(" --> "+str(elem) ,end="")
                    queue.append(elem)



class Graph_Adjancy_Matrix:
    nodes = 0
    adjancy_matrix = []
    def __init__(self,nodes):
        self.nodes = nodes
        for i in range(0,nodes):
            self.adjancy_matrix.append([False]*nodes)
    def insert(self,v1,v2):
        if v1 < self.nodes and v2 < self.nodes and v2 >= 0 and v1 >=0:
            self.adjancy_matrix[v1][v2] = True
            self.adjancy_matrix[v2][v1] = True
    def print(self):
        for i in range(0,self.nodes):
            print(str(i)+" --> "+str(self.adjancy_matrix[i]))
    def delete(self, v1,v2):
        if v1 < self.nodes and v2 < self.nodes and v2 >= 0 and v1 >=0:
            self.adjancy_matrix[v1][v2] = False
            self.adjancy_matrix[v2][v1] = False

    def bfs(self,vertex):
        queue = []
        visited = [False] * self.nodes
        print(vertex,end="")
        visited[vertex] = True
        queue.append(vertex)
        while len(queue) != 0:
            vertex = queue.pop(0)
            for i in range(0,self.nodes):
                if visited[i] == False and self.adjancy_matrix[vertex][i]:
                    print(" --> "+str(i),end="")
                    visited[i] = True
                    queue.append(i)















g=Graph_Adjancy_List(6);
g.insert(1,5)
g.insert(3,5)
g.insert(4,5)
g.insert(2,5)
g.insert(0,1)
g.print()
print("-"*75)
g.bfs(0)



