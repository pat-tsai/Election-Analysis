import datetime as dt
import csv
import os

# direct path to file location
#file_to_load = 'Resources/election_results.csv'

# indirect path to file location
file_to_load = os.path.join("Resources", "election_results.csv")

# output file
file_to_save = os.path.join("analysis", "election_analysis.txt")
print(file_to_save)
total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ''
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data, open(file_to_save, "w") as outfile:

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

    results = (
        f"Election Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")

    # prints election results to terminal
    print(results, end="")

    # writes election results to output file
    outfile.write(results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = votes / total_votes * 100

        candidate_result = (f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

        outfile.write(candidate_result)

        # prints candidate result to terminal
        print(candidate_result)

        if candidate_votes[candidate_name] > winning_count:
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage

    print(f"The winner is {winning_candidate}, who received {winning_count:,} votes accounting for {winning_percentage:.2f}% of all votes.")


#with open(file_to_save, "w") as outfile:



#print(candidate_options)
#print(total_votes)
# creating output document

