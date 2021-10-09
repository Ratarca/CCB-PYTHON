"""
Statement With
Type files : csv / json / parquet
 - Csv
  > writer (writerow / writerows)

"""
import os,sys
import csv
import random

filePath = lambda : os.path.dirname(sys.argv[0])
createData = lambda : {"ID":random.randint(0, 3**7), "LIFE":random.randint(0, 3**7)}

# Write line by line
with open(filePath() + "\\fileOne.csv", 'w' ) as fp:
    writer = csv.writer(fp)
    data = list(createData().values())
    writer.writerow( data )

# Write many rows
with open(filePath() + "\\fileTwo.csv", 'w' ,encoding='UTF-8') as fp:
    writer = csv.writer(fp)

    writer.writerow(['ID','LIFE']) #Create header

    data = [ list(createData().values()) for x in range(10)]
    writer.writerows( data )

# Write by dict (MOST INDICATE!)
with open(filePath() + "\\fileThree.csv", 'w' ,encoding='UTF8', newline='') as fp:
    writer = csv.DictWriter(fp,fieldnames=['ID','LIFE'])

    writer.writeheader()

    data = [ list(createData().values()) for x in range(10)]
    writer.writerows(data)