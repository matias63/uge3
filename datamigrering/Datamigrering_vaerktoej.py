import sys  
import csv
import argparse
import re

### NOTE:
# .csv to .txt converter
# outputs a text file that keeps .csv format
# input file must be .csv
# Checks for correct data in columns
# Checks that data is correctly incerted for the column type
# Any number of columns can be inserted and in any order as long as the header types match the available options 
# deletes empty rows
# Invalid rows are printed in terminal
# output .txt file is named after the .csv file
###


### Run the program - convert .csv to .txt
def main():
    try:
        # Check if the user provided a single input file
        if len(sys.argv) > 2:
            raise ValueError("Provide only 1 file")
        if len(sys.argv) < 2:
            raise ValueError("Provide a file to convert")
    except ValueError as e:
        print(e)
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Simple program to greet the user.")
    # Adding arguments
    parser.add_argument("file", type=str, help="File to read")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    csvfile = args.file
    convert_csv_to_txt(csvfile)



### Converts a .csv file to a .txt file with the same name (keeps headsers and rows with correct data)
### Columns can be inserted in any order and amount as long as the header types match the available options  
def convert_csv_to_txt(csvfile):
    file_type = csvfile[-4:] # read file type
    newfile = f"./{csvfile[:-4]}.txt" # output file (named after input file)
    
    # containers to check regular expressions with
    mail =  r'^[A-Za-z0-9]+([._][A-Za-z0-9]+)?[@][A-Za-z0-9]+[.][A-Za-z]{2,3}$' # regex for email used later
    float_int = re.compile('\d+(\.\d+)?') # regex for float or int used to calc amount or price
    try:
        # Check if the file is a .csv file
        if file_type.lower() != ".csv":
            raise ValueError(f"The input needs to be .csv, not {file_type}")
        if csvfile:
                # open and closes file 
                with open(csvfile, 'r') as file, open(newfile, 'w', encoding='utf-8') as output:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        # get column headers
                        list_of_column_names = row
                        output.write(str(row)+"\n")
                        break
                    for row in csv_reader:
                        try:
                            for i in range(len(row)):
                                for j in range( len(list_of_column_names)): # only checks for data if the right amount of columns or less are present
                                    if len(row[j]) == 0: # check if row is empty: skip it
                                        raise ValueError(f"Empty row: {row}")
                                    if ("_id" in list_of_column_names[j] or "ID" in list_of_column_names[j] or " id" in list_of_column_names[j]) and j==i: # check if columnheaders are id and that id are integers 
                                        try:
                                            int(row[i]) # check if id is an unsigned digit                                          
                                        except ValueError:
                                            raise ValueError(f"ID is not an integer in row: {row}")      
                                    if "name" in list_of_column_names[j] and j==i:   
                                        try:
                                            if isinstance(row[i], str):
                                                row[i] = row[i].strip() # remove whitespace
                                                if " " in row[i] and "@" not in row[i] and "." not in row[i]: # check if element contains a first- and last-name and isnt an email
                                                    ...
                                        except ValueError:
                                            raise ValueError(f"Name is not a string in row: {row}")
                                    if "mail" in list_of_column_names[j] and j==i: # check if element is an email
                                        try:
                                            if isinstance(row[i], str):
                                                if re.match(mail, row[i]):
                                                    ...
                                        except ValueError:
                                            raise ValueError(f"Mail is not an email in row: {row}")
                                    if ("amount" in list_of_column_names[j] or "price" in list_of_column_names[j]) and j==i: # check if element is an amount (float or int)
                                        try:
                                            if isinstance(row[i], str):   
                                                if re.match (float_int, row[i]):
                                                    output.write(str(row)+"\n")
                                        except ValueError:  
                                            raise ValueError (f"Amount is not a float or int in row: {row}")
                        except Exception as e:
                            print(f"An error occurred: {e}") # display ValueErrors
                            continue   # if Valueerror encountered: skip the row
    
     # FilenotFoundError is redundant, since checked in main args, but added for code standards
    except FileNotFoundError:
        print(f"Error: The file '{csvfile}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sys.exit(1)
       

if __name__ == '__main__':
    main()

