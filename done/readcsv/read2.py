import csv
import pandas

with open("./bwq.csv", 'r') as file:
  # csvreader = csv.reader(file)
  csvreader = csv.DictReader(file, delimiter='\t')

  # next(csvreader)

  for row in csvreader:
    # print(row)
    # print(row[0])
    print(row["Beach Name"])

## Pandas
# data = pandas.read_csv("bwq.csv")
# print(data)

# for col in data:
#     print(col)
