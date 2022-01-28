# Nandini Kandi
# This is an example for sort by sales

n = open("reduceOut03.txt","r")  # open file, read-only
s = open("sortBySalesOut.txt", "w") # open file, write
lines = n.readlines() 

amount_location = {}
amount = 0.0
location = ""

for line in lines:
    dataList = line.strip().split('\t') 
    if len(dataList) == 2:       
        location, amount = dataList 
        amount_location[amount] = location # assign sales and locations into key value pairs

#sort using keys
for amount in sorted (amount_location, key = float, reverse=True):
    s.write(amount_location[amount] + '\t' + amount +'\n') # write into output file

n.close()
s.close()