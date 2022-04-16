# election-analysis

## Overview of Election Audit
An analysis of a recent congressional election requested by a Colorado Board of Elections employee, in order to retrieve the following:

1. The total number of votes cast.
2. A breakdown of votes by county in the district.
3. The county with the highest turnout in the district.
4. A complete list of candidates who received votes.
5. The total number of votes each candidate received.
6. The percentage of votes each candidate won.
7. The winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code 1.66.2

## Election-Audit Results

### Total Votes


- There were 369,711 votes cast in the congressional election, retrieved from the raw results data using the following method:

```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1
```

### Results by County

- The three counties involved in this congressional election were:
  
  - Jefferson

  - Arapahoe

  - Denver

Using the following method, a breakdown of votes and percentage of votes by county was retrieved:

```
for row in reader:
  if county_name not in county:
    county.append(county_name)
    county_votes[county_name] = 0
  county_votes[county_name] += 1

for county_name in county_votes:
  cvotes = county_votes.get(county_name)
  cvote_percentage = float(cvotes) / float(total_votes) * 100
```

- This revealed that the highest turnout by county was:
  -  **Denver County**, with *306,055* votes, *82.8%* of the vote.

### Results by Candidate

- The candidates were:

   - Charles Casper Stockham
  
   - Diana DeGette
  
   - Raymon Anthony Doane

Using the following method, the total votes and percentage of votes received per candidate was retrieved:

```
for candidate_name in candidate_votes:
  votes = candidate_votes.get(candidate_name)
  vote_percentage = float(votes) / float(total_votes) * 100
```
  
 - The candidate results were:
 
   - Charles Casper Stockham received 85,213 votes, 23.0% of the vote.
  
   - Diana DeGette received 272,892 votes, 73% of the vote.
  
   - Raymon Anthony Doane received 11,606 votes, 3.1% of the vote.

And the winner was determined using the following method:

```
if (votes > winning_count) and (vote_percentage > winning_percentage):
  winning_count = votes
  winning_candidate = candidate_name
  winning_percentage = vote_percentage
```
  
 - Therefore, the winner of the election was:
 
   - **Diana DeGette** with *272,892* votes, *73%* of the vote.
  
## Election-Audit Summary

In summary, I propose the script used in analyzing this election could easily be used (with minor modifications) to determine the results of any election, given the raw voting data. 
- Point the `file_to_load` variable to the correct path for your `election_results.csv` file. 
 - `file_to_load = os.path.join("folder_with_results", "election_results.csv")`
- Simplify the candidate and county list variables into one dictionary that holds the key-value pair of the candidate and votes per county, then simplify the two separate for loops into one, using the `max()` function.
