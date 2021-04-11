import csv
from typing import Mapping

file = open("python\教程\selenium教程\chap7\city.csv", "r", encoding='utf-8', errors='ignore')
csv_file = csv.reader(file)

for i in csv_file:
    print(i)

header=["name","gender","score"] 
file_1=["zhang_san","male","100"] 
file_2=["Li_si","male","80"]

file = open("python\教程\selenium教程\chap7\city.csv", "w", newline="")
csv_file = csv.writer(file)

csv_file.writerow(header)
csv_file.writerow(file_1)
csv_file.writerow(file_2)

file.close()