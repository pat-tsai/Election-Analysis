import datetime as dt
import csv
import os

# direct path to file location
#file_to_load = 'Resources/election_results.csv'

# indirect path to file location
file_to_load = os.path.join("Resources", "election_results.csv")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ''
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # stores election data as the file_reader object
    file_reader = csv.reader(election_data)

    # skips 1st row (header) of data
    headers = next(file_reader)
    print(headers)

    # prints out each row in a list
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # Creating candidate vote tracker
            candidate_votes[candidate_name] = 0

            # incrementing tracker
        candidate_votes[candidate_name] += 1

        #print(row)


print(candidate_votes)

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = votes / total_votes * 100
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the total vote")

    if candidate_votes[candidate_name] > winning_count:
        winning_candidate = candidate_name
        winning_count = votes
        winning_percentage = vote_percentage

print(f"The winner is {winning_candidate}, who received {winning_count:,} votes accounting for {winning_percentage:.2f}% of all votes.")

#print(candidate_options)
#print(total_votes)
# creating output document
file_to_save = os.path.join("analysis", "election_analysis.txt")

outfile = open(file_to_save, "w")
#outfile.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
outfile.close()