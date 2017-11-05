import sys
filename = open("templates/firstReadInTest.block")
lines = [line.split() for line in open(filename.read().split("\n")) if line]
#
# for line in lines[:]:
#     input = chr(line[0], 0)
#     print(line)

# lines = filename.read().split("\n")

print(lines)