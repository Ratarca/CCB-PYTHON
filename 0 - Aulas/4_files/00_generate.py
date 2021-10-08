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
# Write many rows
# Write by dict