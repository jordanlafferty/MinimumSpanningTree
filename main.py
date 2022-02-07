import csv
import timeit



class Graph:
    def __init__(self):
        pass

    def readCSVFiles(self):
        v = []
        with open("graph.csv", 'r', newline='') as file:
            theReader = csv.reader(file, delimiter=',')
            for rows in theReader:
                r = []
                for y in rows:
                    r.append(int(y))
                v.append(r)
        return v

    def read(self, v):  # graph.read([])
        self.data = v
        self.size = len(v)

    def findMinimum(self, E):  # how to optimize HW
        val = E[0]
        #p = val[[2]].idxmin()
        #val = E[p]
        #x = sorted(E, key=itemgetter(2))
        for i in range(len(E)):
            #if E[i][2] == 1:
               # return E[i]
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


    #not correct
    def process2(self):
        T = [False] * self.size  # [False, false, false...., false}
        L = []  # edge[ vertexIDa , vertexIDb, vertexIDc...]
        E = []

        # do the algorithm
        for i in range(self.size):
            index = 0
            if i == 0:
                T[i] = True
            for j in range(self.size):
                    if i != j:
                        if index == 0:
                            index = [i, j, self.data[i][j]]
                            y = index[2]
                        elif y > self.data[i][j]:
                            index = [i, j, self.data[i][j]]
                            y = index[2]

            targetEdge = index
            L.append(targetEdge)
            #T[targetEdge[0]] = True
            #T[targetEdge[1]] = True
            E = []

        # output
        print(L)
        length = 0
        for ele in L:
            length = length + ele[2]
        print("MSP length is: ", length-1)

    #works correctly
    def process3(self):
        T = [False] * self.size  # [False, false, false...., false}
        L = []  # edge[ vertexIDa , vertexIDb, vertexIDc...]

        # do the algorithm
        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                index =-1
                for j in range(self.size):
                    for k in range(self.size):
                        if T[j] != T[k]:
                            if index == -1:
                                index = [j, k, self.data[j][k]]
                                y = index[2]
                            elif y > self.data[j][k]:
                                index = [j, k, self.data[j][k]]
                                y = index[2]


                L.append(index)
                T[index[0]] = True
                T[index[1]] = True
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
print(timeit.Timer(g.process).timeit(number =10))
print(timeit.Timer(g.process3).timeit(number =10))
