# https://snap.stanford.edu/data/higgs-twitter.html
import networkx as nx
import re

# Create empty Graph
G = nx.DiGraph()

rt_dist = []
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
        print(connection)
        G.add_edges_from([connection])

        print(G.in_degree())
        break

f.close()
