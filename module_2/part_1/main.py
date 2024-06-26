import get_links
import main_webpage_download
import os
import re
import links_extract

# Function to save links to a text file
def link_save(links,type):
    
    # Write the links back to the text file
    with open(type+'_links.txt', 'w') as file:
        for link in links:
            file.write(link + '\n')

def divide_links(links):
    # Download HTML files into respective folders
    R_links = set()
    T_links = set()

    for link in links:
        
        match_response = re.search(r'_to_the_COVID-19_pandemic_in_\w+_\d{4}', link)
        match_timeline = re.search(r'_of_the_COVID-19_pandemic_in_\w+?_?\d{4}', link)
        
        if match_response:
            R_links.add(link)
        elif match_timeline:
            T_links.add(link)

    link_save(R_links, "response")
    link_save(T_links, "timeline")

def main():
    
    main_webpage_download.main()
    links = get_links.main()
    divide_links(links)
    links_extract.main()
    



if __name__ == '__main__':
    main()