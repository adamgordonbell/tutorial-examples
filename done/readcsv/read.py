import csv
import pandas

data = pandas.read_csv("bwq.csv")
print(data)

for col in data:
    print(col)

# with open("bwq-small.tsv", 'r') as file:
#     csvreader = csv.DictReader(file, delimiter="\t")

#     for row in csvreader:
#         print(row["Turbidity"])
#         # print(row[5])