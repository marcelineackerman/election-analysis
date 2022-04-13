# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

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

# Open the election results and read the file.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read and print the header row.

    headers = next(file_reader)

    print(headers)

    # Print each row in the CSV file.

    for row in file_reader:

        # Add to the total vote count.

        total_votes += 1

         # Print the candidate name from each row.

        candidate_name = row[2]

        # Add the candidate_name to the candidate_options list using the append() method
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

# Print the total votes

print(total_votes)

# Print the candidate_options list.

print(candidate_options)


    
