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

num_to_start_from = 129
vertex_set = collatz(num_to_start_from)
vertex_set_as_str = [str(x) for x in vertex_set]

# Construct a graph with 3 vertices
n_vertices = len(vertex_set)
edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (3, 4)]
g = ig.Graph(n_vertices, edges)

# Set attributes for the graph, nodes, and edges
g["title"] = "Small Social Network"
g.vs["name"] = vertex_set_as_str
g.vs["gender"] = ["M", "F", "F", "M", "F"]
g.es["married"] = [False, False, False, False, False, False, False, True]

# Set individual attributes
# g.vs[1]["name"] = "Kathy Morillas"
# g.es[0]["married"] = True

# Plot in matplotlib
# Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    g,
    target=ax,
    layout = g.layout_reingold_tilford(mode="in", root=[0]), # print nodes in a circular layout
    vertex_size=0.1,
    vertex_color=["steelblue" if gender == "M" else "salmon" for gender in g.vs["gender"]],
    vertex_frame_width=4.0,
    vertex_frame_color="white",
    vertex_label=g.vs["name"],
    vertex_label_size=7.0,
    edge_width=[2 if married else 1 for married in g.es["married"]],
    edge_color=["#7142cf" if married else "#AAA" for married in g.es["married"]]
)

plt.show()

# Save the graph as an image file
fig.savefig('social_network.png')