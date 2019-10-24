log_file = open("um-server-01.txt") #this loads a file called 'um-server-01' to build sales information from


def sales_reports(log_file): # initializes script to process log into sales report
    for line in log_file: # loops through each item in the log
        line = line.rstrip() # applies a function to remove any whitespace in line of report
        day = line[0:3] # records the first three chars as the day of week sale was made
        
        if day == "Mon": # checks if the day matches the sales info wanted

        # changed 'Tue' to 'Mon'
            print(line) # prints out relevant sales data for desired day of week


sales_reports(log_file) # runs function to select relevant sales for a given week day
