import numpy as np
import pandas as pd
import csv

file = open("TRN", 'r')
data = file.read()

data = data.replace("\t", ",")

csv_file = open("trn.csv", "w")
csv_file.write(data)
