# https://snap.stanford.edu/data/higgs-twitter.html
import networkx as nx
import re

# Create empty Graph
G = nx.DiGraph()
# print(G)
# rt_dict = {}

# lines = network_file.read().splitlines()

# To DO: 1/15/2019
# To show growth of network over time, must first sort by timestamps

# Create dictionary, keyed by timestamp, to store all Retweet network connections
# being made over time

# rt_network = []
rt_network = dict()

with open("../data/higgs-activity_time_sample.txt") as f:
    for line in f:
        # split tweet activity line into list
        # [id of tweeter, id of retweeter, timestamp, mention or retweet indicator]
        # ^^ Double check the tweeter, retweeter id ^^
        activity = line.strip().split()
        # print(activity[3])
        # Only target Retweets
        if activity[3] == 'RT':
            time = re.sub("[^0-9]", "", activity[2]) # remove random letters in Unix timestamp
            tweeter = activity[0]
            retweeter = activity[1]
            # Create a tuple to hold each individual node connection
            connection = tuple((tweeter, retweeter))

            if time in rt_network.keys():
                # print("time:", time)
                rt_network[time].append(connection)

                # Add nodes/edges to our DiGraph
                # G.add_edges_from(rt_network[time])
                # print(nx.info(G))
                # print(rt_network)
            else:
                # Add newly generated tweet dictionary to retweet network dictionary
                rt_network[time] = [connection]

                # Add nodes/edges to our DiGraph
                # G.add_edges_from(rt_network[time])
                # print(nx.info(G))

# print(nx.degree(G))
# print(type(rt_network))


# Create dictionary to hold Kin distribution at each time entry
in_degree_dists = dict()

# For each time entry in our 'retweet network' dictionary, add nodes/edges
for time in rt_network:
    # Add nodes/edges created from retweets at that timestamp
    # print("time:", time)

    # Empty dictionary to hold distribution data
    in_dist = []
    G.add_edges_from(rt_network[time])

    # Generate in-degree distribution at that timestamp
    # print(G.in_degree())
    for degree in G.in_degree():
        in_dist.append(degree[1])
        # print(degree[1])
    # print("time: ", time, ", dist: ", sorted(in_dist))

    in_degree_dists[time] = sorted(in_dist)

    print(in_degree_dists)
    # print(nx.info(G))
    # print(G.in_degree())
    # print(sorted(set(G.in_degree().values())))
    # print("time:", time, rt_network[time])
# print(nx.info(G))
            # Add edges to Graph
            # G.add_edges_from([connection])
            # Print degrees of G
            # print("info of G:", nx.info(G))

# print(rt_network)
            # print("time: ", time, ", connection:", connection)

# Print degrees of G
# print("info of G:", nx.info(G))

# Iterate over Twitter dictionary by timestamp and calculate network statistics at each step
