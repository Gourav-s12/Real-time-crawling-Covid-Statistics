import subprocess
import os
from datetime import datetime
import re

def list_files(folder_path):
    try:
        # Get a list of all folders (subdirectories) in the specified folder
        subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        
        # Get a list of all files in the specified folder
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Get a list of all files in each subfolder
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            files.extend([os.path.join(subfolder_path, f).replace('\\', '/') for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))])


        return files
    except OSError as e:
        print(f"Error: {e}")
        return None
    
def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
        return date_obj
    except ValueError:
        print("Incorrect date format, please enter date in dd-mm-yyyy format.")
        return None
    
all_countries = []
def main():
    print("************************************")
        
    while True :

        choice = input("a. News in given range \n"
                    "b. Responses in given range \n"
                    "q. go back to previous menu: \n"
                    )
        if choice == 'q' :
            break

        date1 = input("Input Starting Date [dd-mm-yyyy format] : ") # "22-10-2021"
        start_date = validate_date(date1)
        date2 = input("Input Ending Date [dd-mm-yyyy format] : ") # "22-12-2023"
        end_date = validate_date(date2)

        if start_date is None or end_date is None : 
            print("Invalid Date Format ")
            continue

        if choice == 'a' : 
            process_call(start_date, end_date, what = "timeline")

        elif choice == 'b' : 
            process_call(start_date, end_date, what = "response")
        
        else : 
            print("Invalid Input ")

def process_call(start_date, end_date, what = "response"):
    folder_path = "../../../module_2/part_1/"+what+"/"
    file_list = list_files(folder_path)
    if len(file_list) == 0:
        print("no file found , you should load the data first in the main menu")
        return 

    command = f" ( python3 mapper.py {file_list[0]} | "
    # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    # getting year
    match_re = re.search(r'/\w+/(\d{4})/', file_list[0])
    year = match_re.groups()[0]

    for file in file_list[1:]:

        command = command + f" sort | python3 combiner.py {start_date} {end_date} {year} ) && ( python3 mapper.py {file} | "
        # process = subprocess.Popen(command, shell=True, stdin=process.stdout, stdout=subprocess.PIPE)

        # getting year
        match_re = re.search(r'/\w+/(\d{4})/', file)
        year = match_re.groups()[0]

    command = command + f" sort | python3 combiner.py {start_date} {end_date} {year} ) | sort "
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE) # subprocess.Popen(command, shell=True, stdin=process.stdout, stdout=subprocess.PIPE)

    command = " python3 reducer.py "
    process = subprocess.Popen(command, shell=True, stdin=process.stdout, stdout=subprocess.PIPE)
    
    output, _ = process.communicate()
    print(f"\n{what} for {start_date} to {end_date} - ")
    print("\n" + output.decode())

if __name__ == '__main__':
    main()
               