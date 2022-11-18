#!/usr/bin/python3

import os
import csv

data_dir = "data"             # The name of the folder with the CSVs
output_file = "results.csv"

with open(output_file, "w") as ofp:
  writer = csv.writer(ofp)
  writer.writerow([
    "School name in full",
    "Teacher's name",
    "Teacher Contact e-mail",
    "Contact phone",
    "School URN (see https://exams.bpho.org.uk)",
    "School Postcode",
    "Date of sitting Section 1",
    "Date of sitting Section 2",
    "Start Time",
    "End Time",
    "First name",
    "Surname",
    "Gender",
    "Year Group",
    "Physics",
    "Astro",
    "Any specific candidate info:",
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Comments"
  ])
  for file in os.listdir(data_dir):
    if not file.endswith(".csv"):
      continue
    with open(os.path.join(data_dir, file), "r", encoding="ISO-8859-1") as fp:
      data = csv.reader(fp)
      lines = list(line for line in data)
      school_data_1 = lines[8][:4]
      school_data_2 = lines[11][:6]
      for line in lines[16:]:
        if all([len(x) == 0 for x in line]):
          continue
        extended_line = school_data_1+school_data_2+line
        writer.writerow(extended_line)