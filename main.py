import csv


class Graph:
    def __init__(self):
        pass

    def readCSVFiles(self):
        v = []
        with open("graph.csv", 'r', newline='') as file:
            theReader = csv.reader(file, delimiter=',')
            for rows in theReader:
                r = []
                for x in rows:
                    r.append(int(x))
                v.append(r)
        return v;

    def read(self, v):  # graph.read([])
        self.data = v
        self.size = len(v)

    def findMinimum(self, E):  # how to optimize HW
        val = E[0]
        for i in range(len(E)):
            if val[2] > E[i][2]:
                val = E[i]
        return val

    def process(self):
        T = [False] * self.size  # [False, false, false...., false}
        L = []  # edge[ vertexIDa , vertexIDb, vertexIDc...]
        E = []

        # do the algorithm
        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(self.size):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                targetEdge = self.findMinimum(E)
                L.append(targetEdge)
                T[targetEdge[0]] = True
                T[targetEdge[1]] = True
                E = []

        # output
        print(L)
        length = 0
        for ele in L:
            length = length + ele[2]
        print("MSP length is: ", length)


g = Graph()
x = g.readCSVFiles()
g.read(x)
g.process()
