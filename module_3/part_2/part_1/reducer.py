import sys

date_curr = None
total_val = ""

for line in sys.stdin:
    if ":-" in line:
        # print(line)
        date, val = line.strip().split(":-")
        if date == date_curr:
            total_val = val + total_val
        else:
            if date_curr is not None:
                print(f"{date_curr} : {total_val}\n")
            total_val = val
            date_curr = date

# Handle the last date outside the loop
if date_curr is not None:
    print(f"{date_curr} : {total_val}\n")

