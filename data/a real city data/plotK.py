"""
画出电力拓扑图，包括节点注入功率和边的K值。
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
g.es["k"] = kv[:]
g.vs["name"] = [i+1 for i in range(len(g.vs))]
g.vs["p"] =[0,0,0,-4.57142857142857,-4.57142857142857,-4.57142857142857,-4.57142857142857,-4.57142857142857,-3.14285714285714,-3.42857142857143,-2.28571428571429,-2.28571428571429,-3.42857142857143,-3.42857142857143,-5.14285714285714,-3.42857142857143,-3.42857142857143,-3.42857142857143,-2.57142857142857,-3.42857142857143,-6.85714285714286,-4.57142857142857,-3.42857142857143,-5.14285714285714,-4,-4.57142857142857,-4.57142857142857,-4.57142857142857,9.50665585190133,2.24247340044849,2.9820125005964,23.8561000047712,1.52679040030536,2.14227778042846,10.2223388520445,4.9739968509948,2.38561000047712,10.1925187270385,0.834963500166993,1.14509280022902,12.405172002481,7.8725130015745,1.46715015029343,0.596402500119281,5.64793167612959]


igraph.plot(g,
            vertex_label=[ str(g.vs["name"][i]) + str(" :") + str("{:.2f}".format(g.vs["p"][i])) for i in range(n)],
            #vertex_size=26,
            #vertex_label_size=16,
            #edge_label=g.es["k"],
            bbox=(1600,1200)
            )
