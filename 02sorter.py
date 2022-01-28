# Nandini Kandi
# This is an example for sorter

n = open("out01.txt","r")  # open file, read-only
s = open("sortedOut02.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()