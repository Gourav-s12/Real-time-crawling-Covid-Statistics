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


## Project Description:

The project is divided into 4 modules. 
- Module 1 : Crawling Covid-19 statistics from the website https://www.worldometers.info/coronavirus/ (for all countries and individual countries over a period of time)
  - part 1  : Extracting the worldwide total cases, Active cases, Total deaths, Total recovered, Total tests, Death/million, Tests/million, New case, New death, New recovered.
  - part 2  : Extracting each countries Active cases, Daily death, New Recovered, New cases, etc.

- Module 2 : Crawling Covid-19 news wiki page https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic containing date wise text data of the Covid-19 news and also for multiple countries.
  - part 1  : Extracting the worldwide news and responses for all times.
  - part 2  : Extracting the news and responses for a particular country over a period of time.

- Module 3 : 
    - part 1  : Using NOSQL database to give the results of the statistics and news in a structured format for the queries related to MODULE 1 
    - part 2  : Using NOSQL database to give the results of the statistics and news in a structured format for the queries related to MODULE 2

- Module 4: Combining the entire project and creating a menu driven for the user to interact with the database and get the required information.

## Contributors

- Gourav Sarkar (Roll NO: 23CS60R01)
  - Crawled worldometers website for each countries Active cases, Daily death, New Recovered, New cases, etc. (module 1 part 2, module 3 part 1.2)
  - Crawled Wikipedia for Covid-19 timeline and response data (module 2 part 1, module 3 part 2.1)
  - main file menu

- Bibek Pal (Roll NO: 23CS600R39)
  - [Will be added]

- Aditya Srivastav (Roll No: 23CS60R15)
  - [Will be added]

# Work done

## Module 1 

- Part 2: 
- Extract the data for the 4 fields mentioned for a particular country mentioned in worldmeters_countrylist.txt . The grammars are mentioned in the file 'extract_activecases.py' , 'extract_newcases.py' , 'extract_newdeaths.py' and 'extract_newrecoveries.py' . After that the outputs are stored into output folder with each country having 4 files like-
Australlia_active_case.txt , Australlia_new_case.txt , Australlia_daily_death.txt , Australlia_new_recovered.txt .

*NOTE* All countries mentioned in worldmeters_countrylist.txt are do not have all of the 4 fields. Some Countries may have 3 or fewer files.

- run :
- Run 'main.py' then choose 'a. data load'


## Module 2 

- Part 1: 
- To obtain all the required Wikipedia webpages, we first download the main wiki page using Mainpage_download.py. From the main wiki page, we extract all the timelines and response pages present on that page using links_extract.py. Finally, using extract_info_timeline.py and extract_info_response.py, we extract all the response pages one by one, categorized by their respective month names, which are then organized inside their respective years. We store the data within timeline and response folder, as format of - DATE: Info in each row. Here, each year is a folder and they have 12 files in them as for each months.

- run :
- Run 'main.py' then choose 'a. data load'


## Module 3.1 

- Part 2 : 
- display the details of 4 fields of a particular country. The user is asked about the name of the country as well as start and end date. The country, start date and end date are written in a file which is to be feed into the mapper. Also all country names are written in a file which is to be feed into the mapper along with date. The mapper passes the data to the reducer which inturn preprocess and filters and send it to the reducer for the final output.The logic of closest country in respect to percentage change is also done int the reducer. 

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

- Part 1 : 
- Displays all the worldwide responses given a time range. The user is asked about (start and end date). All the responces were extracted and saved in module 2. Given the time range, goes through all the subfolders and extracts all txt files which are inbetween those time range and puts all text in a single txt file. This is then fed to mapper. The mapper passes the data to the reducer which preprocess the data and sends it to the reducer for the final output.

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

2021-11-26  :   The United Kingdom, European Union, and United States have imposed travel restrictions on eight southern African countries including South Africa, Botswana, Zimbabwe, Namibia, Lesotho, Eswatini, Mozambique, and Malawi in order to contain the spread of the B.1.1.52 \(Omicron\) Variant.South African Minister of HealthJoe Phaahlahas objected to the travel restrictions on South Africa, defending South Africa's handling of the pandemic and describing travel bans as against the norms and standardsof the World Health Organization.

2021-12-17  :   The World Health Organizationissued an emergency use listing (EUL) for NVX-CoV2373, expanding the basket of WHO-validated vaccines against the SARS-CoV-2 virus.

```
