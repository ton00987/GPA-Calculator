import csv

all_grade = {}

with open('Calculate GPA.csv', 'r') as f:
  reader = csv.reader(f)
  next(reader)
  for row in reader:
    print(row)