import csv

with open('sources/ibdb/ibdb_id.csv', newline='') as f:
    data = list(csv.reader(f))[0]

noDuplicateLIst = list(set(data))

with open('sources/ibdb/noduplicatesIbdb.csv', 'w') as f:
    for id in noDuplicateLIst:
        f.write(id+',')
