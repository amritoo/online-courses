# Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of
# mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the
# person who sent the mail. The program creates a
# Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to
# find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    if line.startswith('From '):
        sender = line.split()[1]
        count[sender] = count.get(sender, 0) + 1

large_num = None
large_sender = None

for k, v in count.items():
    if large_num is None or v > large_num:
        large_num = v
        large_sender = k

print(large_sender, large_num)
