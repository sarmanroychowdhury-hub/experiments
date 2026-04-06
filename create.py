import json
import csv

with open('file.json') as file:
    data = json.load(file)

with open ('Output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(data[0].keys())

    for row in data:
        writer.writerow(row.values())

print("Conversion successful")  

#make output.csv file so that it writes the output there