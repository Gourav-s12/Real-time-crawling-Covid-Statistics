import os
import re
from ply import lex, yacc
from urllib.request import Request, urlopen
import webpage_download
import extract_info_response
import extract_info_timeline

# Function to save links to a text file
def extract_links(link, what):
        
    if what == "response":
        match_response = re.search(r'_to_the_COVID-19_pandemic_in_(\w+)_(\d{4})', link)
        month, year = match_response.groups()
        
    elif what == "timeline":
        match_timeline = re.search(r'_of_the_COVID-19_pandemic_in_(\w+)?_?(\d{4})', link)
        month, year = match_timeline.groups()
        if not month:
            month = ""
            
    else:
        return
    
    # Adjust file_name based on the presence of month
    if month:
        file_name = f"{month}_{year}.html"
    else:
        file_name = f"{year}.html"

    print(f"processing info from: {file_name}")
    
    # geting the data
    webpage_download.main(link)
    if what == "response":
        extract_info_response.main(file_name, what)
    else:
        extract_info_timeline.main(file_name, what)

def main():
    
    with open('response_links.txt', 'r') as file:
        for line in file:
            extract_links(line, "response")
            
    print()
    with open('timeline_links.txt', 'r') as file:
        for line in file:
            extract_links(line, "timeline")

    

if __name__ == '__main__':
    main()