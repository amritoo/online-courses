from sys import argv, exit
import csv
import re


def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    # end if

    with open(argv[1]) as csv_file:
        f = csv.reader(csv_file, delimiter=",")
        fields = next(f)[1:]
        # print(fields)

        file = open(argv[2], "r").read()
        num = [max_str(x, file) for x in fields]
        # print(num)

        for row in f:
            ar = [int(x) for x in row[1:]]
            if ar == num:
                print(row[0])
                break
            # print(ar)
        else:
            print("No match")
# end def


def max_str(sub, string):
    reg = "(?=((" + re.escape(sub) + ")+))"
    matched = re.findall(reg, string)
    if len(matched) == 0:
        return 0
    else:
        return max(len(m[0]) // len(sub) for m in matched)
# end def


main()
