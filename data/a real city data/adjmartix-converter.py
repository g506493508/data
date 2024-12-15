"""
将边表示的电力拓扑(DY-edges.csv)和通信拓扑(DYcom-edges.csv)转换成仿
真程序使用的邻接矩阵形式。
"""
import csv
import math
import igraph
import random

fprefix = "DY"
fsuffix = "-edges.csv"
fname = fprefix+fsuffix
foutname = fprefix+".csv"

edges = []
with open(fname, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        row_int = []
        for x in row:
            row_int.append(int(x)-1) # igraph index starts from zero
        edges.append(row_int)

n = max([ max(edge) for edge in edges ]) +1
g = igraph.Graph()
g.add_vertices(n)
g.add_edges(edges)

#g.get_adjacency()
g.write_adjacency(foutname, sep=',')
