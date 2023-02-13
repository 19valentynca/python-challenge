import os

import csv

# path to collect the csvfile
csvFilePath = os.path.join("..","PyPoll", "election_data.csv")

# open our csv file
with open(csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    # skip the header
    heading = next(csvReader)
    # set a running total for the number of votes
    num_votes = 0
    # find all the row values for candidates
    candidate_array = []
    # we will cut this array down later

    # use a for loop to use our running total to get the number of votes
    # and to get all our row candidate values
    for row in csvReader:
        num_votes += 1
        candidate_array.append(str(row[2]))


    total = 1
    # set our comparison value
    pace = candidate_array[0]
    # create to empty arrays to append to for our totals for each candidatea and the groupings of votes
    specific_candidate_array = []
    total_array = []
    # set our starting index
    i = 1
    # run a while loop to index through all the rows
    while i < (num_votes):
        # then compare to the previous row value to see if we have a new candidate
        if candidate_array[i] == pace:
            # if we have the same candidate, add one to their vote total
            total += 1
        else:
            # else we save that candidate into our grouping array and start the total over for the next candidate
            specific_candidate_array.append(str(pace))
            total_array.append(int(total))
            pace = candidate_array[i]
            total = 1
        # keep the index moving forward
        i += 1
    
    # now lets find our total number of groupings for candidates
    num_diffs = 0
    for row in specific_candidate_array:
        num_diffs += 1
        # this will give us all the groupings we have in our created array
    
    # now lets cut the goupings down to only the overall candidates
    filtered_array = []
    # run a for loop to create this new array
    for k in specific_candidate_array:
        if k not in filtered_array:
            filtered_array.append(k)
            # using the 'not in' operator we can only add new candidates and eliminate the repeats we had in the grouping array
    # now lets get the number of candidates
    cand_list = []
    num_new_rows = 0
    # num new rows will be our running total of candidates
    for row in filtered_array:
        num_new_rows += 1
        if row not in cand_list:
            cand_list.append(row)
    
    # to find the sums of voted from the earlier groupings, we need some nested loops
    # start with creating an emtpy array to store new total votes in
    untitled_array = []
    # and our comparison value
    pace = specific_candidate_array[0]
    # and this will be our running total that will reset for every new candidate
    total = total_array[0]
    # our index values for both
    i = 1
    j = 1
    # and tick will be our index to stop the loop from starting at the same startpoint
    tick = 1
    while j < (num_diffs):
        i = tick
        while i >= tick and i < (num_diffs):
            if specific_candidate_array[i] == pace:
                # add to the candidates vote running total
                total += total_array[i]
            
            i += 1
        # add the candidates vote totals to the empty array
        untitled_array.append(total)
        # change the pace so that we move to the next candidate
        pace = specific_candidate_array[tick]
        # start the total over and to the next candidate
        total = total_array[tick]
        j += 1
        tick += 1
    
    # now lets clean our created array to only have as many values as we have candidates
    x = len(untitled_array)
    while x > num_new_rows:
        #.pop() function eliminates the unneeded extra values
        untitled_array.pop(x-1)
        x -= 1
    
    # finally we will run one last while loop to get our percentages
    # set an index value
    y = 0
    # create a percentage array for all candidates
    percentages = []
    while y < num_new_rows:
        # multiply by 100 to get into percent form
        untitled = 100 * (untitled_array[y]/num_votes)
        # round it to the requisite 3 decimal places
        untitled = round(untitled,3)
        # and then add each percentage to the empty array
        percentages.append(untitled)
        y += 1
    # and find the max percentage to fin who won
    z = percentages.index(max(percentages))
    # you could also do this by vote total, either or

    # and then crown the winner
    winner = cand_list[z]
    

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {num_votes}")
    print("------------------------")
    print(f"{cand_list[0]}: {percentages[0]}% ({untitled_array[0]})")
    print(f"{cand_list[1]}: {percentages[1]}% ({untitled_array[1]})")
    print(f"{cand_list[2]}: {percentages[2]}% ({untitled_array[2]})")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")

    # to create a text file
    outputFilePath = os.path.join("..", "PyPoll", "PyPollOutput.txt")
    lines = ["Election Results", "------------------------", f"Total Votes: {num_votes}",
             "------------------------", f"{cand_list[0]}: {percentages[0]}% ({untitled_array[0]})",
             f"{cand_list[1]}: {percentages[1]}% ({untitled_array[1]})",
             f"{cand_list[2]}: {percentages[2]}% ({untitled_array[2]})", "------------------------",
             f"Winner: {winner}", "------------------------"]
    with open(outputFilePath, "w") as txtOutput:
        for line in lines:
            txtOutput.write(line)
            txtOutput.write("\n")