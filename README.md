# Election-Analysis

## Overview of Election Audit
In the exercises building up to this challenge, we were instructed to create code that would calculate total number of votes cast, complete list of candidates participating, votes and percentage of votes each candidate received, and determine the winner of the election based on popular vote. In this challenge, we were instructed to add additional functionality to the existing code, including voter turnout from each county, percentage of each votes from each county, and county with highest turnout.  


## Election-Audit Results
Shown below is the terminal output for the election results:

![Screenshots](Resources/election_results.PNG)
- The total number of votes cast in this election was 369,711
- Out of the total number of votes, Jefferson county provided 38,855 (10.5%), Denver county provided 306,055 (82.8%), and Arapahoe provided 24,801 (6.7%)
- Denver county had the largest number of votes
- Candidate vote breakdown is as follows:
  - Charles Casper Stockham: 85,213 (23.0%)
  - Diana DeGette: 272,892 (73.8%)
  - Raymon Anthony Doane: 11,606 (3.1%)
 - Diana DeGette was the winner of the elction, receiving 272,892 or 73.8% of the total votes


## Election-Audit Summary: modifying the script for more applications
Currently, the script is only able to analyze datasets located at the path "Resources/election_results.csv", as shown by the code `file_to_load = os.path.join("Resources/election_results.csv")`. We could make the following modifications to allow for more flexibility in the input file: 
```
input_path = input("Enter dataset path: ")
file_to_load = os.path.join(input_path)
```
By making these changes, we can allow the user to specify the location of a dataset anywhere on their computer, as well as analyze any number of datasets. 

Futhermore, the current script has hardcoded values for both the candidate and county option lists and votes dictionaries. Since we want to script to analyze election results, we will always require candidate info so we can leave those values hardcoded. However, in other elections, instead of finding statistics for counties we may want to analyze voter participation by state, ethnicity, or age. We can account for these additional factors by once again taking user input with the following code, and placing a variable inside the f-strings to output the appropriate name:


old code: 
```python
# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# 2: Track the largest county and county voter turnout.
highest_county_name = ''
highest_county_turnout = 0
...
...
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
        
    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (f"\n-------------------------\nLargest County Turnout: "
                              f"{highest_county_name}\n-------------------------\n")
    print(winning_county_summary)
```

modified code:
```python
# 1: Create a generic list and votes dictionary.
var1_options = []
var1_votes = {}

# accounting for any input variable
var1 = input("Enter desired factor to be analyzed: ")

# 2: Track the largest user input variable and voter turnout.
var1_highest = ''
var1_turnout = 0

...
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
---->   f"{var1} Votes:\n")
        
    # 7: Print user input var with the largest turnout to the terminal.
    winning_county_summary = (f"\n-------------------------\nLargest {var1} Turnout: "
---->                         f"{var1_highest}\n-------------------------\n")
    print(winning_county_summary)
```
