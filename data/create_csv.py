import numpy as np
import pandas as pd
import csv
from functools import reduce

file = open("TRN", 'r')
data = file.readlines()

data = list(map(lambda x: x.replace("\t", ","), data[:10001]))

csv_data = reduce((lambda x, y: x+y), data)

csv_file = open("trn.csv", "w")
csv_file.write(csv_data)
