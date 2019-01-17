# https://snap.stanford.edu/data/higgs-twitter.html
import networkx as nx
from collections import Counter
import numpy as np
import os
import re

# Set up 'split files' data directory
data_dir = "../data"



rt_dist = []


for file in sorted(os.listdir(data_dir + "/split_files")):
    counter = 0
    # Create empty Graph for each file
    G = nx.DiGraph()
    if file.endswith(".txt"):
        # print(file)
        with open(data_dir + "/split_files/" + file) as f:
        # with open("../data/higgs-activity_time_sorted_RT.txt") as f:
            for line in f:
                # split tweet activity line into list
                # [id of tweeter, id of retweeter, timestamp, mention or retweet indicator]
                # ^^ Double check the tweeter, retweeter id ^^
                activity = line.strip().split()

                tweeter = activity[0]
                retweeter = activity[1]
                # Create a tuple to hold each individual node connection
                connection = tuple((tweeter, retweeter))
                # print(connection)
                G.add_edges_from([connection])

                # print(G.in_degree())
                #
                # counter += 1
                #
                # if counter == 20:
                #     break

        f.close()
# print("# of nodes in G:", nx.number_of_nodes(G))
# print("G.in_degree(): ", G.in_degree())
        # Create list of nodes and degrees
        degs = [d[1] for d in G.in_degree()]
        counts = list(set([(deg, degs.count(deg)) for deg in degs]))
# counts.sort()
# print("counts: ", counts)
# print("sorted counts: ", sorted(counts))

# [(0, 9), (1, 5), (2, 1), (3, 1)]



    print("degs:", degs)
    print("counts: ", counts)
    # print("Counter(degs).most_common(): ", Counter(degs).most_common())
    # print("degree_invcumsum(sorted(counts)):", degree_invcumsum(sorted(counts)))
    # print("degree_invcumsum(Counter(degs).most_common()):", degree_invcumsum(Counter(degs).most_common()))



    with open(data_dir + "/split_files/node_dists/node_dist" + file, 'w+') as output:
        # output.write(str(degree_invcumsum(sorted(counts))))
        output.write(str(degs))
    output.close()
# print(degree_invcumsum(sorted(counts)))
# For each tuple, sum number of degrees for each subsequent tuple in sorted degree counts list

# print("degs: ", degs)
# Create x, y values for plotting
# x = possible degrees a node can have
# y = number of nodes with degree >= x
# We will create plot of log(x), log(y)

# Create list of all possible degrees, from min to max
#x = list(range(max(degs)+1))
# x = [count[0] for count in counts]
# Create list of inverse cumulative degree distributions
# y = [sum([c[1] for c in counts[i:]]) for i in range(len(counts))]
# print("x: ", x)
