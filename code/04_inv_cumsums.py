import os
from collections import Counter

data_dir = "../data/split_files/node_dists"
out_dir = "../data/cumsum_dists"

# Empty list to create cumulative distributions
cum_deg_list = []

def degree_invcumsum(dcounts):
    # Ensure list of counts is sorted
    dcounts = sorted(dcounts)

    # Empty list to store
    invcum_dist = []

    # Enumerate tuples of (degree, number of nodes with that degree)
    for idx, count in enumerate(dcounts):
        # initialize empty variable to track inverse cumulative sum
        inv_cumsum = 0
        # print("idx: ", idx, "count: ", count)
        # print("dcounts[idx]: ", dcounts[idx])
        # print("dcounts[idx:]: ", dcounts[idx:])
        # For every tuple, sum all the ndegree counts for subsequent tuples
        for n, ndegs in dcounts[idx:]:
            inv_cumsum += ndegs
        # print("n: ", n, " ndegs: ", ndegs, " inv_cumsum: ", inv_cumsum)
            # print("ndegs:", ndegs)
        # Append inverse cumulative count to the list
        invcum_dist.append((dcounts[idx][0], inv_cumsum))
    # print("degree counts list: ", dcounts)
    # print("inv cumsum: ", invcum_ dist)
    return(invcum_dist)

for file in sorted(os.listdir(data_dir)):
    if file.endswith(".txt"):
        # print(file)
        with open(data_dir + "/" + file) as f:
        # with open("../data/higgs-activity_time_sorted_RT.txt") as f:
            for line in f:
                deg_dist = eval(line)[1:25]
                # print(deg_dist)
                # print(type(eval(line)))
                cum_deg_list.extend(deg_dist)
                # print("cum_deg_list: ", cum_deg_list)
                print("---------")
                print("length cum_deg_list: ", len(cum_deg_list))
                print(degree_invcumsum(Counter(cum_deg_list).most_common()))
                print("---------")
        # with open(data_dir + "/split_files/" + file) as f:
        # # with open("../data/higgs-activity_time_sorted_RT.txt") as f:
        #     for line in f:
        #         print(line)
