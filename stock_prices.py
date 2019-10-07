Month = 0
AdjC = 5
Vol = 6

def get_file():
    ''' Returns a file stream, else prints an error message '''
    filename = input("Enter filename: ")
    try:
        openfile = open(filename, "r")
        return openfile
    except:
        print("Filename {} not found!".format(filename))


def get_data_list(data_file):
    '''
    Gets the file stream and makes a list
    Start with an empty list for line_str in data_file:
        strip end-of-line, split on commas, and append items to
    '''
    data_list = [ ]
    for line_str in data_file:
        data_list.append(line_str.strip().split(','))
    return data_list


def get_monthly_averages(x):
    ''' Calcutales the monthly averages '''
    count = 1 # The Count goes through all the sublists in the main list (x) from get_data_list()
    averagelist = []
    while True:
        average1 = 0
        average2 = 0
        date = x[count][Month]
        currdate = date[0:7] # Gets the current month
        averagelist.append(currdate)

        while True:
            if count >= len(x):
                break
            newdate = x[count][Month]
            nextdate = newdate[0:7] # A checker for if we are still working with the same month, if not: break
            if currdate != nextdate:
                break
            else:
                average1 = average1 + (float(x[count][Vol])*float(x[count][AdjC]))
                average2 = average2 + float(x[count][Vol])
            count += 1

        averagelist.append(average1/average2)
        if count >= len(x):
            break

    return averagelist


def get_max(x):
    ''' Calculates the highest price for the entire file '''
    count = 0 # Constants and lists to work with
    max = 0
    adj_close = []
    date = []
    highest_list = []
    the_date = ""

    for line in x: # Going over the filestream and making two list for adj close and date
        adj_close.append(line[AdjC])  
        date.append(line[Month])
    date.remove(date[Month]) 
    adj_close.remove(adj_close[Month])
    float_adj_close = [float(i) for i in adj_close]
    for i in float_adj_close:
        if i > max:
            max = i # Finding max price
            the_date = date[count]
        count += 1	

    highest_list.append(the_date)
    highest_list.append(max)
    return highest_list # Making a list with date and price


def print_average(averagelist):
    ''' Prints the averages with formatting '''
    print("{:<10s}{:>7s}".format("Month", "Price"))
    for i in range(0,len(averagelist),2):
        print('{:<10s}{:>7.2f}'.format(averagelist[i], round(averagelist[i+1], 2)))


def print_highest(highest_list):
    ''' Prints the highest price and date with formatting '''
    print("Highest price {:.2f} on day {}".format(round(float(highest_list[1]),2), highest_list[0]))


def main():
    ''' Main program starts here '''
    openfile = get_file()
    if openfile:
        
        newlist = get_data_list(openfile)

        averagelist = get_monthly_averages(newlist)

        highest_list = get_max(newlist)

        print_average(averagelist)

        print_highest(highest_list)

main()
