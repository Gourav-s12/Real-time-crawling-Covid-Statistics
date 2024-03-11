import sys 
from datetime import datetime

date1 = sys.argv[1]
date2 = sys.argv[2]
year = sys.argv[3].strip()

start_date = datetime.strptime(date1.strip(), "%Y-%m-%d")
end_date = datetime.strptime(date2.strip(), "%Y-%m-%d")

for line in sys.stdin: 
    if ":-" in line:
        # print(line.strip())
        # print(len(line.strip().split(":-")))
        date , val = line.strip().split(":-")
        try :
            curr_date = datetime.strptime(date.strip() + " " + year, "%m-%d %Y")
        except : 
            print("Error as the space seperated strings cannot be treated as Integers")
            continue

        if curr_date >= start_date and curr_date <= end_date and val is not None and val != "":
            # print(curr_date.strftime("%Y-%m-%d"))
            print(f"{curr_date.strftime('%Y-%m-%d')} :- {val}")