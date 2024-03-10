#!/usr/bin/env python3
import sys
from datetime import datetime

file_name = None 
index = 0
try : 
    file_name = sys.argv[1]
    country_name = sys.argv[2]
    country_name = country_name.strip()
    with open(file_name, 'r') as file:
        for line in file:
            date, val = line.strip().split(",")
            print(f"{date} {country_name} {val}")
except : 
    print(f"Error in Mapper ..{line}")

# python3 mapper.py "../../worldometer/Results/new_recovered/india.txt" india | sort -n | python3 combiner.py 2020-02-20 2020-02-2021 && python3 mapper.py  "../../worldometer/Results/new_recovered/canada.txt" canada | sort -n | python3 combiner.py 2020-02-20 2020-02-2021 | sort -n | python3 reducer.py india