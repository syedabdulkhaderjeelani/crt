class graphmatrix:
    def _init_(self,size=None,adjmatrix=None):
        if adjmatrix is not None:
            self.adjmatrix = adjmatrix
            self.size = len(adjmatrix)
        else:
            self.size = size
            self.adjmatrix = [[0 for _ in range(size)] for _ in range(size)]
    def addedge(self, u, v):
        if u< self.size and v < self.size:
            self.adjmatrix[u][v] = 1
            self.adjmatrix[v][u] = 1
    
    def display(self):
        print("Adjacency Matrix:")
        for row in self.adjmatrix:
            print(" ".join(map(str, row)))

dj_matrix=[
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]
g = graphmatrix(adjmatrix=dj_matrix)
g.display()
