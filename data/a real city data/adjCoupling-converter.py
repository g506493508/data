"""
将边表示的电力线路比例容量c转换成仿
真程序使用的邻接矩阵K形式。
"""
import csv
import math
import igraph
import random

fprefix = "DY"
fsuffix = "-edges-K.csv"
fname = fprefix+fsuffix
foutname = fprefix+"-K"+".csv"

edges = []
kv = []
with open(fname, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        edge_int = []
        k_float = []
        for i in range(2):
            edge_int.append(int(row[i])-1) # igraph index starts from zero
        k_float = float(row[2])
        edges.append(edge_int)
        kv.append(k_float)

n = max([ max(edge) for edge in edges ]) +1
g = igraph.Graph()
g.add_vertices(n)
g.add_edges(edges)
g.es["coupling"] = kv[:]

adjK = g.get_adjacency(attribute="coupling")

# manually write
wf = open(foutname, 'w')
for i in range(n):
    for j in range(n):
        wf.write(str(adjK[i][j]))
        if j < n-1:
            wf.write(',')
        else:            
            wf.write('\n')
wf.close()
