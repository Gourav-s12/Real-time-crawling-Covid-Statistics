#!/usr/bin/env python3
import sys
from datetime import datetime

file_name = None 
index = 0
try : 
    file_name = sys.argv[1]
    print(file_name)
    with open(file_name, 'r') as file:
        for line in file:
            if ":" in line:
                # print(line.strip().split(":"))
                date,val = line.strip().split(":")
                print(f"{date} :- {val}")
except : 
    print(f"Error in Mapper ..{line}")
