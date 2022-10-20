__author__ = "Jonathan Montrose"
__version__ = "1.0.1"
__maintainer__ = "Jonathan Montrose"
__email__ = "jem118@shsu.edu"
__github_repository__ = "https://github.com/jem0ntr053/ISDesign-A03-index/tree/main"


# Write a program to read two lists of names from two input files and then match
# the names in the two lists using Co-sequential Match based on a single loop.
# Output the names common to both the lists to an output file.

def sorting(filename, sorted_filename):
    with open(filename) as infile:
        words = []
        for line in infile:
            temp = line.split()
            for i in temp:
                words.append(i)

    words.sort()
    with open(sorted_filename, "w") as outfile:
        for i in words:
            outfile.writelines(i)
            outfile.writelines("\n")


def cosequential_search():
    sorting("names1.txt", "names1_sorted.txt")
    sorting("names2.txt", "names2_sorted.txt")

    # open the sorted files
    in_file1 = open('names1_sorted.txt', 'r')
    in_file2 = open('names2_sorted.txt', 'r')
    out_file = open('common_names.txt', 'w')

    # read the first name from each file
    name1 = in_file1.readline().rstrip()
    name2 = in_file2.readline().rstrip()

    # loop until both names are empty
    while name1 != '' and name2 != '':
        # if name1 is less than name2
        if name1 < name2:
            # get the next item from file1
            name1 = in_file1.readline().rstrip()
            # if name2 is less than name1
        elif name2 < name1:
            # get the next item from file2
            name2 = in_file2.readline().rstrip()
        else:
            # write the common name to the output file
            out_file.write(name1 + '\n')
            # get the next item from both files
            name1 = in_file1.readline().rstrip()
            name2 = in_file2.readline().rstrip()

    # close the files
    in_file1.close()
    in_file2.close()
    out_file.close()


if __name__ == '__main__':
    cosequential_search()
