import pandas as pd

# Load the CSV file into a pandas dataframe
df = pd.read_csv('vote.csv')

# Create a dictionary to store the vote counts
vote_counts = {}

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Get the candidate's name and first and second choice
    candidate = row['candidates']
    first_choice = row['first_choice']
    second_choice = row['second_choice']

    # If the candidate's first choice is not already in the vote count dictionary, add it with a count of 0
    if first_choice not in vote_counts:
        vote_counts[first_choice] = 0

    # If the candidate's second choice is not already in the vote count dictionary, add it with a count of 0
    if second_choice not in vote_counts:
        vote_counts[second_choice] = 0

    # Increment the vote count for the candidate's first choice
    vote_counts[first_choice] += 1

    # If the candidate's first choice did not win, increment the vote count for their second choice
    if vote_counts[first_choice] < vote_counts[max(vote_counts, key=vote_counts.get)]:
        vote_counts[second_choice] += 1

# Print out the final vote counts
print(vote_counts)