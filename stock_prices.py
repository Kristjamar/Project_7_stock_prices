def get_file():
    filename = input("Enter filename: ")
    try:
        openfile = open(filename, "r")
        return openfile
    except:
        print("Filename {} not found!".format(filename))


def get_data_list(data_file):
    data_list = [ ]	    # start with an empty list for line_str in data_file:
    for line_str in data_file:
        # strip end-of-line, split on commas, and append items to
        data_list.append(line_str.strip().split(','))
    return data_list


def get_monthly_averages(x):
    count = 1
    print("{:<10s}{:>7s}".format("Month", "Price"))

    for i in range(1,13):
        
        average1 = 0
        average2 = 0
        date = x[count][0]
        currdate = date[0:7]
        while True:
            try:
                newdate = x[count][0]
                nextdate = newdate[0:7]
            except:
                nextdate = currdate

            if currdate != nextdate:
                break
            else:
                try:
                    average1 = average1 + (float(x[count][6])*float(x[count][5]))
                    average2 = average2 + float(x[count][6])
                except:
                    break
            count += 1

        print('{:<10s}{:>7.2f}'.format(currdate, round(average1/average2, 2)))


def main():

    openfile = get_file()
    if openfile:
        
        newlist = get_data_list(openfile)

        get_monthly_averages(newlist)

main()
