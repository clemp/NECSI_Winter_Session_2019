# https://snap.stanford.edu/data/higgs-twitter.html
import networkx as nx
from collections import Counter
import re

# Create empty Graph
G = nx.DiGraph()

rt_dist = []

counter = 0
with open("../data/split_files/higgs-activity_time_sorted_RT00.txt") as f:
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

        counter += 1

        if counter == 10:
            break

f.close()
print("# of nodes in G:", nx.number_of_nodes(G))

# Create list of nodes and degrees
degs = [d[1] for d in G.in_degree()]
counts = list(set([(deg, degs.count(deg)) for deg in degs]))
counts.sort()
print(counts)

# Create x, y values for plotting
# x = possible degrees a node can have
# y = number of nodes with degree >= x
# We will create plot of log(x), log(y)
