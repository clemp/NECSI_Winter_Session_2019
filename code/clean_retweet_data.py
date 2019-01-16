# https://snap.stanford.edu/data/higgs-twitter.html

# Clean original higgs twitter activity file to filter for only retweets
with open("../data/higgs-activity_time_sample.txt") as fin, open("../data/higgs-activity_time_retweets.txt", "w+") as fout:
    for line in fin:

        activity = line.strip().split()
        # Only target Retweets
        if activity[3] == 'RT':
            fout.write(line)
