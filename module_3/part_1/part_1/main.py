import subprocess
import os
import get_countries
   
all_countries = []
def main():
    global all_countries
    countries = get_countries.main()
    print("************************************")
        
    while True :
        choice = input("\nChoose an option:\n"
                        "a. Get Worldometer Country Covid Statistics  \n"
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
        process_call(country)

def process_call(country):
    file_name_prefix = "../../../module_1/part_1/"
    file_name = file_name_prefix +"text.txt"

    print(f"filename - {file_name}")
    
    try:
        open(file_name, 'r')
    except:
        print(f"{country} does not have the record, maybe load the data from the main menu")
        return 

    command = f" python3 mapper.py {file_name} {country} | python3 combiner.py | python3 reducer.py "
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    output, _ = process.communicate()
    print(f"for {country} data - ")
    print("\n" + output.decode())

if __name__ == '__main__':
    main()
               