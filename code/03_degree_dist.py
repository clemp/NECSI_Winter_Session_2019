# https://snap.stanford.edu/data/higgs-twitter.html
import networkx as nx
from collections import Counter
import numpy as np
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
print("G.in_degree(): ", G.in_degree())
# Create list of nodes and degrees
degs = [d[1] for d in G.in_degree()]
counts = list(set([(deg, degs.count(deg)) for deg in degs]))
# counts.sort()
# print("counts: ", counts)
print("sorted counts: ", sorted(counts))

# [(0, 9), (1, 5), (2, 1), (3, 1)]

def degree_invcumsum(dcounts):
    # Ensure list of counts is sorted
    dcounts = sorted(dcounts)
    
    # Empty list to store
    invcum_dist = []

    # Enumerate tuples of (degree, number of nodes with that degree)
    for idx, count in enumerate(dcounts):
        # initialize empty variable to track inverse cumulative sum
        inv_cumsum = 0
        print("idx: ", idx, "count: ", count)
        print("dcounts[idx]: ", dcounts[idx])
        print("dcounts[idx:]: ", dcounts[idx:])
        # For every tuple, sum all the ndegree counts for subsequent tuples
        for n, ndegs in dcounts[idx:]:
            inv_cumsum += ndegs
        print("n: ", n, " ndegs: ", ndegs, " inv_cumsum: ", inv_cumsum)
            # print("ndegs:", ndegs)
        # Append inverse cumulative count to the list
        invcum_dist.append((dcounts[idx][0], inv_cumsum))
    print(invcum_dist)
    return(invcum_dist)
degree_invcumsum(sorted(counts))
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
