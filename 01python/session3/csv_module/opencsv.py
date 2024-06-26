import csv
import pprint
reader = csv.reader(open(r'session3\csv_module\trycsv.csv','r'))
mydic={}
for line in reader:
    mydic[line[0]]={'age':line[1], 'city':line[2], 'country': line[3]}


pprint.pprint(mydic)