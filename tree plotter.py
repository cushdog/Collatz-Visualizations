import igraph as ig
import matplotlib.pyplot as plt

# #functions to return the nodes in the tree
def collatz(num):
    list = []
    ## add current number to list and set num to next number in seq
    while num > 1:
        list.append(num)
        num = collatz_helper(num)
    ## loop breaks when num = 1 --> add 1 to list here
    list.append(1)
    return list

## returns next number in sequence
def collatz_helper(num):
    if (num % 2 == 0):
        return int(num / 2)
    else:
        return 3 * num + 1

num_to_start_from = 13
vertex_set = collatz(num_to_start_from)
vertex_set_as_str = [str(x) for x in vertex_set]


#compute the size of the nodes
node_size = 25 * 0.05
print(node_size)

# print(vertex_set)
index_of_start = vertex_set.index(num_to_start_from)
g = ig.Graph(n = len(vertex_set), directed=True)
fig, ax = plt.subplots(figsize=(5,5))
g.add_edges([(1,0),(2,1), (0,3)])
g.vs["label"] = vertex_set_as_str
layout = g.layout_reingold_tilford(mode="all", root=[index_of_start])

ig.plot(g, target=ax, layout=layout, vertex_size=node_size, vertex_label_size=7)
plt.show()