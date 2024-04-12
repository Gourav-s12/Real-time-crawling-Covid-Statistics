import subprocess
import os
from datetime import datetime
import get_countries

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
        return date_obj
    except ValueError:
        print("Incorrect date format, please enter date in dd-mm-yyyy format.")
        return None
    
all_countries = []
def main():
    global all_countries
    countries = get_countries.main()
    print("************************************")
        
    while True :
        choice = input("\nChoose an option:\n"
                        "a. Change in active cases in %\n"
                        "b. Change in daily death in %\n"
                        "c. Change in new recovered in %\n"
                        "d. Change in new cases in %\n"
                        "q. go back to previous menu: \n"
                    )
        if choice == 'q' :
            break
        
        country = input("\nEnter Name of the Country : ")
        country = country.strip().replace(" ","_")

        found = False
        all_countries = []
        for _, country_list in countries.items():
        # Iterate through countries in each continent
            all_countries.extend(country_list)
            if country in country_list:
                found = True

        if found is not True:
            print("Invalid country\n valid countries are- \n")
            print(all_countries)
            continue

        date1 = input("Input Starting Date [dd-mm-yyyy format] : ") # "22-10-2023"
        start_date = validate_date(date1)
        date2 = input("Input Ending Date [dd-mm-yyyy format] : ") # "22-12-2023"
        end_date = validate_date(date2)

        if start_date is None or end_date is None : 
            print("Invalid Date Format ")
            continue

        if choice == 'a' : 
            process_call(country, start_date, end_date, what = "active_case")

        elif choice == 'b' : 
            process_call(country, start_date, end_date, what = "daily_death")
            
        elif choice == 'c' : 
            process_call(country, start_date, end_date, what = "new_recovered")
            
        elif choice == 'd': 
            process_call(country, start_date, end_date, what = "new_case")
        
        else : 
            print("Invalid Input ")

def process_call(country, start_date, end_date, what = "daily_death"):
    file_name_prefix = "../../../module_1/part_2/output/"
    file_name = file_name_prefix + country+"_"+what+".txt"
    
    try:
        open(file_name, 'r')
    except:
        print(f"{country} does not have a {what} record, maybe load the data from the main menu")
        return 

    command = f" ( python3 mapper.py {file_name} {country} | "
    # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    for coun in all_countries:
        if coun == country:
            continue
        file_name = file_name_prefix + coun+"_"+what+".txt"
        try:
            open(file_name, 'r')
        except:
            continue

        command = command + f" sort | python3 combiner.py {start_date} {end_date} ) && ( python3 mapper.py {file_name} {coun} | "
        # process = subprocess.Popen(command, shell=True, stdin=process.stdout, stdout=subprocess.PIPE)

    command = command + f" sort | python3 combiner.py {start_date} {end_date} ) | sort "
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE) 

    command = f" python3 reducer.py {country} {what}"
    process = subprocess.Popen(command, shell=True, stdin=process.stdout, stdout=subprocess.PIPE)
    
    output, _ = process.communicate()
    print(f"{what} for {country} for {start_date} to {end_date} - ")
    print("\n" + output.decode())
if __name__ == '__main__':
    main()
               