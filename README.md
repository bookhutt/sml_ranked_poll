# sml_ranked_poll
The South Mud Lake Ranked Poll Calculator

## Description

A simple-to-use tool for calculating the results of a ranked vote style poll. A ranked poll is where those being asked for their opinion get two or more votes, first choice, second choice, etc. There's numerous ways to set up a ranked poll, but for the purposes of settling The South Mud Lake Open Space renaming issue it seemed prudent to keep things as simple as possible to start. 

Our poll took place in an agreed opon area surrouding the open space. The poll was conducted by hand. 65 Households in the neighbobrhood were visited. 39 Neighbors in 23 of those households registered an opinion. A breif description of each candidate name was given, along with the option for those being polled to nominate a name of their choice. 

This tool was designed to tabulate the results of that poll. It also tabulates first-past-the-post results.

## Method
The script calculates the second place votes by dividing the second_choice_total column by 2. It then combines the first and second place votes using the add method, with the fill_value=0 parameter ensuring that any candidates with no second place votes are still included in the total.

Finally, the script determines the winner by finding the candidate with the most total votes using the idxmax method, and prints out the winner's name and vote count.

## Ethic

This is an example of instant-runoff voting where voters rank candidates in order of preference. The second-choice votes are weighted less than the first-choice votes, but they still count as preferences and can influence the outcome of the poll.

Critics may say that polling of this nature can lead to strategic voting and other chicanery. However, many would say it leads grants a more nuanced view into folks opinions and the preferences of the majority.

Ultimately, the ethics of any poll come down to transparancy and open discussion.

Following the withdrawl of Tammy Forrest, the original winner of the poll and the changing of two votes, the poll is now based on the vote_totals_5_18.csv file

### Dependencies

* python
* pandas

### Executing program

* make sure you have a completed 'vote_totals.csv' file in the same folder as the script
* type: python sml_ranked_poll.py

### Outcome
The ranked order winner is Moose Meadows with 9.0 votes!
The pass-the-post winner is Moose Meadows with 8 votes!


