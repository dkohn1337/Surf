## Create Python list for using in loops from CSV
## Below package must be installed via pip

import csv

result = []
with open("/path to csv file goes here","r") as CSV_file:
    csv_reader=csv.reader(CSV_file)
    for line in csv_reader:
        result.extend(line)
print(result)