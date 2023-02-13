import os

import csv

# path to collect the csv file content
csvFilePath = os.path.join("..","PyBank", "budget_data.csv")

# open up our csv file and set it with a variable
with open(csvFilePath) as csvFile:
    # read the csv file and give the reader a variable
    csvReader = csv.reader(csvFile, delimiter=",")
    # move past the header row to our data
    heading = next(csvReader)
    # set the months running total
    num_months = 0
    # set the profits/losses running total
    prof_losses = 0
    # create an array to append each profits/losses row value to
    PFL_array = []
    # create an array to append each month row value to
    months_array = []

    # creating a for loop to get a months array and profits/losses array
    for row in csvReader:
        # sum the total number of months by using a running total
        num_months += 1
        months_array.append(str(row[0]))
        # sum the profits/losses by adding each row value to the running total
        prof_losses += int(row[1])
        # append to the profits/losses array
        PFL_array.append(int(row[1]))
    # set a variable to have the first profits/losses value
    # so that we can set up a difference tracker
    diff_starter = int(PFL_array[0])
    
    # create an empty differences array
    diff_array = []
    diff_array.append(int(PFL_array[0]))
    
    # set a ticker value to run a while loop
    i = 1
    # set the interval of our row index
    while i >= 1 and i <= (num_months - 1):
        # use the i index profits/losses value and subtract the previous value from it
        row_end = int(PFL_array[i]) - diff_starter
        # add that value to our differences array
        diff_array.append(row_end)
        # reset the previous value for the next index
        diff_starter = PFL_array[i]
        # add one to the index ticker
        i = i + 1
        # print(diff_array)
    
    # repeat the ticker process to get the sum
    # then use that sum and row count to find the average
    j = 1
    # total will be our running sum
    total = 0
    while j >= 1 and j <= (num_months - 1):
        # each index adds to the running sum
        total += diff_array[j]
        # set the index forward
        j += 1

    # find the average using our created variables    
    average = total/(num_months - 1)
    
    # repeat the process AGAIN for the max profit value
    k = 2
    # set a tracker of the index where the max value is
    # we use this to trace back to the month
    tracker1 = 2
    # give the running max a starting value to test against
    pace1 = diff_array[1]
    # we use index 1 because the first difference we observe is between index 0 and index 1
    while k >= 2 and k <= (num_months - 1):
        # create another variable to connect with the running max
        test = diff_array[k]
        # use an if loop to collect a running max
        if test >= pace1:
            # sets our running max to the new larger value
            pace1 = test
            # sets our running index to that row value where the max is at
            # again this is to trace back to the necessary month
            tracker1 = k
        k += 1
    # connect the index to the matching month of the max
    great_gain = months_array[tracker1]
    
    # run the entire process again for the min profits/losses value
    l = 2
    tracker2 = 2
    pace2 = diff_array[1]

    while l >= 2 and l <= (num_months - 1):
        test = diff_array[l]

        if test <= pace2:
            pace2 = test
            tracker2 = l
        l += 1
    
    # now get the months value connected to the min
    great_loss = months_array[tracker2]

    print("Financial Analysis")
    # print a line to show the start of calculated values
    print("-------------------------")
    # prints the total number of months
    print(f"Total Months: {num_months}")
    # prints the summation of profits/losses from all rows
    print(f"Total: ${prof_losses}")
    # prints the average to 2 decimal places
    print("Average Change: $" + "%.2f" % average)
    # prints the profits/losses max with the connected month
    print(f"Greatest Increase in Profits: {great_gain} (${pace1})")
    # prints the profits/losses min with the connected month
    print(f"Greatest Decrease in Profits: {great_loss} (${pace2})")

    # to create a text file
    outputFilePath = os.path.join("..", "PyBank", "PyBankOutput.txt")
    lines = ["Financial Analysis", "-------------------------", f"Total Months: {num_months}",
             f"Total: ${prof_losses}", "Average Change: $" + "%.2f" % average,
             f"Greatest Increase in Profits: {great_gain} (${pace1})",
             f"Greatest Decrease in Profits: {great_loss} (${pace2})"]
    
    with open(outputFilePath, "w") as txtOutput:
        for line in lines:
            txtOutput.write(line)
            txtOutput.write("\n")
       
