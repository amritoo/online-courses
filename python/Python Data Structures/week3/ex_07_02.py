# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence: 0.8475
# Count these lines and extract the floating point values
# from each of the lines and compute the average of those
# values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total, count = 0, 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    pos = line.find(':')
    total += float(line[pos+2:])
    count += 1

# print("Done")
print('Average spam confidence:', total / count)
