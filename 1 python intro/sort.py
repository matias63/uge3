
import sys  
import csv
import argparse
from collections import defaultdict
import matplotlib.pyplot as plt




def main():
    parser = argparse.ArgumentParser(description="Simple program to greet the user.")
    # Adding arguments
    parser.add_argument("-f","--file", required=True, type=str, help="File to read")
    parser.add_argument("column", type=str, help="column names")

    
    # Parse the command-line arguments
    args = parser.parse_args()

    # read name and length from csv file, by providing the file and the column name in terminal at execution
    csvfile = args.file
    column_names = args.column

    read_file(csvfile, column_names)
    names_dict = read_file(csvfile, column_names)
    
    length_dict = length_sort(names_dict)
    alfabetic_sorted = alfabetic_sort(length_dict)
    counter = count_letters(alfabetic_sorted)



    #printing
    print("sorted by length:\n",length_dict,"\n")
    print("sorted by alfabetic order:\n",alfabetic_sorted,"\n")
    print(counter)

    plot_histogram(counter)

   

### Plotting the histogram
def plot_histogram(counter):
    letters = sorted(counter.keys()) #sorting the order of the histogram
    counts = counter.values()

    plt.bar(letters, counts)

    # Setting Y-axis from 0 to max value
    plt.ylim(0, max(counts))

    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Histogram')
    
    plt.show()

### Read file and return a dictionary with the names and their lengths
def read_file(csvfile, column_names):
    names_dict = {}
    with open(csvfile, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            names_dict[row[column_names].lower()] = len(row[column_names])
    return names_dict


### Sort the dictionary by length of names including spaces
def length_sort(names_dict):
    length_dict = dict(sorted(names_dict.items(), key=lambda item: item[1]))
    return length_dict


### Sort the dictionary by alfabetic order (first name)
def alfabetic_sort(names_dict):
    alfabetic_dict = dict(sorted(names_dict.items()))
    return alfabetic_dict
 

### Count the frequency of each letter in the names
def count_letters(names_dict):
    counter = {}
    for name in names_dict:
        for c in name:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] +=1
    return counter


if __name__ == '__main__':
    main()

