import networkx as nx

# G = nx.DiGraph()

# G.add_nodes_from(['A', 'B','C'])
# G.add_edges_from([('A', 'B'), ('A', 'C')])

# print(nx.info(G))
list = []

dict_a = {'time': "a", 'other': [(30, 20), (29,39)]}
dict_b = {'time': "b", 'other': [(20, 1), (6,3)]}

list.append(dict_a)
list.append(dict_b)

print(list)

test_key = "a"
# [{'test': 'a', 'other': [(30, 20), (29, 39)]}, {'test': 'b', 'other': [(20, 1), (6, 3)]}]

if test_key in [d['time'] for d in list]:
    print("It's in!")
# G.add_edges_from(
#     [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
#      ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
