import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('vote_totals.csv')

# Set the candidate column as the index
df.set_index('candidate', inplace=True)

# Calculate second place votes by dividing the second_choice_total column by 2
second_place_votes = df['second_choice_total'] / 2

# Combine first and second place votes
total_votes = df['first_choice_total'].add(second_place_votes, fill_value=0)

# Determine the winner
winner = total_votes.idxmax()
ptp_winner = df['first_choice_total'].idxmax()

print(f"The ranked order winner is {winner} with {total_votes[winner]} votes!")
print(f"The pass-the-post winner is {ptp_winner} with {df['first_choice_total'][ptp_winner]} votes!")


