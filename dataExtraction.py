import csv


with open('teraterm.log', 'r') as file:
    data = file.readlines()

subString = "111"

line = 0

for i in range(len(data)):
    a = data[i]
    if (data[i].find(subString, 23) != -1):  # no string found returns -1
        line = line + 1
        with open('processedData.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([data[i]])
        print(data[i])

print(line)
