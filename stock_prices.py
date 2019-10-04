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

def main():

    openfile = get_file()
    if openfile:
        
        newlist = get_data_list(openfile)

        print(newlist)
        
main()
