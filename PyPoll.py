# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os
# Assign a variable for the file to load/save from/to a path
file_to_load = os.path.join ("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Declare list: Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        total_votes += 1
#print(total_votes) 
    # Print the candidate name from each row.
        candidate_name = row[2]
    # If the candidate does not match any existing candidate add to the list of candidates.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
#print(candidate_options)
            candidate_votes[candidate_name] = 0
#print(candidate_votes)
        candidate_votes[candidate_name] += 1
#print(candidate_votes)
    #with open(file_to_save, "w") as txt_file:
       # Retrieve votes for each candidate and get precentage of votes
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
            f"--------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------------\n")
print(winning_candidate_summary)
# Use the open statement to open the file as a text file
with open(file_to_save, "w") as txt_file:
    
    election_data.close()




