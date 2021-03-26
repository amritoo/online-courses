import re

print(sum([int(x) for x in re.findall('\d+', open('regex_sum_935908.txt').read())]))

# try:
#     f = open('regex_sum_42.txt')
# except:
#     print('Invalid filename')
#     quit()

# ar = []
# ex = re.compile('\d+')
# for line in f:
#     [ar.append(int(x)) for x in ex.findall(line)]
# print(ar)
# print(sum(ar))
