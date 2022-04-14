# Add our dependencies.

import csv
import os


# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total_votes variable

total_votes = 0

# Declare a new list for candidate names.

candidate_options = []

# Declare an empty dictionary for votes per candidate.

candidate_votes = {}

# Winning candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read header row.

    headers = next(file_reader)

    # Print each row in the CSV file.

    for row in file_reader:

        # Add to the total vote count.

        total_votes += 1

         # Print the candidate name from each row.

        candidate_name = row[2]

        # Add the candidate_name to the candidate_options list using the append() method
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count

            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count

        candidate_votes[candidate_name] += 1

# Open txt file to save results

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end = "")

    txt_file.write(election_results)

# Determine the candidate's percentage of votes

# Iterate through the candidate list

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes)*100

        # Print out each candidate's name, vote count, and percentage of votes

        if (votes > winning_count) and (vote_percentage>winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        # Print each candidate's results to terminal and txt file

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning  Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)



   
