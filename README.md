# Real-time-crawling-Covid-Statistics

## Project : Lex Yacc and NoSQL - crawling Covid Statistics and News

## Repository Link : https://github.com/Gourav-s12/Real-time-crawling-Covid-Statistics

## How to Run

To run this project, ensure that you have `lex` and `ply` installed in your system. Then navigate to the root folder and execute the following command in the terminal:

```bash
python main.py
```

### To run the code in linux-
- you have to make sure within "main.py" in root folder
- change "python main.py" -> "python3 main.py" 
- run "python3 main.py"
- or in "python2" depends on your system

### To run the code in linux-
- you have to make sure within "main.py" in root folder
- change "python3 main.py" -> "python main.py" 
- run "python main.py"

## Contributors

- Gourav Sarkar (Roll NO: 23CS60R01)
  - Crawled worldometers website for each countries Active cases, Daily death, New Recovered, New cases, etc. and handle user queries for this part (module 1 part 2, module 3 part 1.2)
  - Crawled Wikipedia for Covid-19 timeline and response data and Store it in 12 text files each year, handle user queries for this part(module 2 part 1, module 3 part 2.1)
  - main file menu

- Bibek Pal (Roll NO: 23CS60R39)
  - Crawled Wikipedia and extract the news information that is available for the five countries. [not working]

- Aditya Shrivastava (Roll No: 23CS60R15)
  - Crawled worldometers website for each countries Active cases, Daily death, New Recovered, New cases, etc. (module 1 part 1)
  - Addressing Queries of Worldometer Covid Statistics (module 3 part 1.1)
  - main file menu

# Work done

## Module 1 
#### Part 1 [Aditya Shrivastava]: 
- Extract the data for Countries/World/Continent about Covid Statistics from worldometers wikipedia website and storing it in a textfile 
  text.txt.

- run :
- Run 'main.py' then choose 'a. data load'


#### Part 2 [Gourav Sarkar]: 
- Extract the data for the 4 fields mentioned for a particular country mentioned in worldmeters_countrylist.txt with 'option_new_case.py' , 'option_active_case.py' , 'option_new_recovered.py' and 'option_daily_death.py' . After that the outputs are stored into output folder with each country having 4 files like-
Australlia_active_case.txt , Australlia_new_case.txt , Australlia_daily_death.txt , Australlia_new_recovered.txt .

*NOTE* All countries mentioned in worldmeters_countrylist.txt do not have all of the 4 fields. Some Countries may have 3 or fewer files.

- run :
- Run 'main.py' then choose 'a. data load'


## Module 2 

#### Part 1 [Gourav Sarkar]: 
- To obtain all the required Wikipedia webpages, we first download the main wiki page using Mainpage_download.py. From the main wiki page, we extract all the timelines and response pages present on that page into timeline.txt and response.txt files. Finally, using extract_info_timeline.py and extract_info_response.py, we extract pages one by one, categorized by their respective month names, which are then organized inside their respective years. We store the data within timeline and response folder, as format of - DATE: Info in each row. Here, each year is a folder and they have 12 files in them as for each months.

- run :
- Run 'main.py' then choose 'a. data load'

#### Part 2 [Bibek Pal]: 
- not updated the readme

## Module 3.1 
#### Part 1 [Aditya Shrivastava]: 
- The user is asked about the name of the country. The statistics of the given country and the world are compared and the
  percentage of the country statistics with respect to that of the world are printed using mapper/combiner/reducer.

- run :
- Run 'main.py' then choose "b. data query" and then 'a. data query - get country info respect to world' and then give asked inputs.


#### Part 2 [Gourav Sarkar]: 
- display the details of 4 types of data of a particular country. The user is asked about the name of the country as well as start and end date. First extract the country, start date and end date are written in a file(mapper) then filter in between those time range(combiner) and send it for the final output(reducer).The logic of closest country in respect to percentage change is also done in the reducer. 

- run :
- Run 'main.py' then choose "b. data query" and then 'b. data query - get changes in countries' and then give asked inputs
- Enter Name of the Country : India
- choose "any option" like- "d. Change in new cases in %"
- Input Starting Date [dd-mm-yyyy format] : "any date" like- 22-10-2023
- Input Ending Date [dd-mm-yyyy format] : "any date" like- 22-12-2023
- output -

```bash
new_case for India for 2023-10-22 to 2023-12-22 -

Increase in India : 338200.0%
Closest Country with Similar Statistics is Malaysia with 349600.0%
```


## Module 3.2

#### Part 1 [Gourav Sarkar]: 
- Displays all the worldwide responses given a time range. The user is asked about (start and end date). All the data were extracted and saved in module 2. Given the time range, goes through all the subfolders and extracts all txt files(mapper) then filter in between those time range(combiner) and puts all text in a single txt optput(reducer).

- run :
- Run 'main.py' then choose "b. data query" and then 'c. data query - get news and response' and then give asked inputs
- Enter Name of the Country : India
- choose "any option" like- "b. Responses in given range"
- Input Starting Date [dd-mm-yyyy format] : "any date" like- 22-10-2021
- Input Ending Date [dd-mm-yyyy format] : "any date" like- 22-12-2021
- output -

```bash
........
.......
2021-11-23  :   South Africa releases a genomic assay showing a record number of mutations -32- on the protein spike of variant B.1.1.52, stoking world-wide alarm given the massive rise in the number of cases in the region and its being on track to overtake the Delta Variant. First discovered from a sample taken in Botswana November 11,the report triggers an emergency WHO meeting on November 26.

2021-11-26  :   The United Kingdom, European Union, and United States have imposed travel restrictions on eight southern African countries including South Africa, Botswana, Zimbabwe, Namibia, Lesotho, Eswatini, Mozambique, and Malawi in order to contain the spread of the B.1.1.52 \(Omicron\) Variant.South African Minister of HealthJoe Phaahlahas objected to the travel restrictions on South Africa, defending South Africa\'s handling of the pandemic and describing travel bans as against the norms and standardsof the World Health Organization.

2021-12-17  :   The World Health Organizationissued an emergency use listing \(EUL\) for NVX-CoV2373, expanding the basket of WHO-validated vaccines against the SARS-CoV-2 virus.

```

#### Part 2 [Bibek Pal]:
- not done  
