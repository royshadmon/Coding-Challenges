"""
Time complexity analysis:

Insert each line into a 2D dictionary in O(n) where n is the total number of lines in the file.
We sort the dates in O(m log m) where m is the total number of unique dates.
We sort the URLs count in in O(m log p) where m is as above and p the total number or unique URLs on a given date.
We print the sorted dictionary in O(mp) which represents the total number of unique date and URL pairs.
Overall, the total run-time is O(n) + O(m log m) + O(m log p) + O(mp).
Therefore, the run-time is O(n).
"""

import time
from operator import itemgetter


def main():

    # Verifying the file actually exists. If not, then return an error without crashing.
    try:
        file = open("input.txt", "r")
    except:
        print("File Doesn't Exist")
        return

    dateURLDict = {}

    for line in file:
        epoch, url = _seperateDateURL(line)
        date = _epochToDate(epoch)
        if date not in dateURLDict:
            dateURLDict[date] = {}
            dateURLDict[date][url] = 1
        elif url not in dateURLDict[date]:
            dateURLDict[date][url] = 1
        else:
            dateURLDict[date][url] += 1

    _printSortedDateUrlDict(dateURLDict)


def _printSortedDateUrlDict (dateURLDict):
    """
    Prints the sorted dictionary
    :param dateURLDict: the 2D dictionary storing the data from the input files
    :return:
    """
    for i in sorted(dateURLDict.items()):
        print(i[0])
        sorted_urls_count = sorted(i[1].items(), key=itemgetter(1), reverse=True)
        for url in sorted_urls_count:
            print (url[0], url[1])


def _seperateDateURL (input):
    """
    This function splits each line from input file by the "|" character
    :param input: A single line from the input file
    :return: The epoch time (int) and URL (string)
    """
    epochURL = input.split("|")
    return int(epochURL[0]), epochURL[1].strip()


def _epochToDate (epoch):
    """
    Converts the epoch to a GMT date
    :param epoch: A single epoch
    :return: A date in GMT (string)
    """
    return time.strftime('%m/%d/%Y GMT', time.gmtime(epoch))


if __name__ == "__main__":
    main()
