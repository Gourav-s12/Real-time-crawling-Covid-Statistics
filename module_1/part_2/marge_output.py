import os
from datetime import datetime

def main(file1, file2):
    # Read the first file with dates
    try: 
        with open('./output/'+file1+'.txt', 'r') as f:
            dates_list = [date.replace('"','') for date in f.read().split('","')]

        # Read only the first line of the second file with values
        with open('./output/'+file2+'.txt', 'r') as f:
            values_line = f.readline().strip().split(',')
    except:
        return

    # Combine dates and values into a list of tuples
    combined_data = list(zip(dates_list, values_line))

    # Create a new list with formatted dates and corresponding values
    result_data = []
    for date, value in combined_data:
        formatted_date = datetime.strptime(date.strip(), "%b %d, %Y").strftime('%Y-%m-%d')
        result_data.append([formatted_date, value.strip()])

    
    # Remove the original files
    # os.remove(f"./output/{file1}.txt")
    # os.remove(f"./output/{file2}.txt")

    # Write the combined data to a new file
    with open('./output/'+file2+'.txt', 'w') as f:
        for formatted_date, value in result_data:
            f.write(f'{formatted_date},{value}\n')

