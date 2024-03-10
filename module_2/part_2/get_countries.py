
def main():
    # Main menu loop
    # Open the text file and read lines
    with open('./cpvid_countrylist.txt', 'r') as file:
        lines = file.readlines()

    # Initialize empty lists for each continent
    India = []
    Malaysia = []
    Australia = []
    Singapore = []
    England = []
    oceania = []

    # Initialize a dictionary to map continents to their respective lists
    continent_lists = {
        "India": India,
        "Malaysia": Malaysia,
        "Australia": Australia,
        "Singapore": Singapore,
        "England": England,
        "Oceania": oceania
    }

    # Flag to identify the current continent
    current_continent = None

    # Iterate through lines and populate continent lists
    for line in lines:
        line = line.strip()
        if line.startswith("India"):
            current_continent = India
        elif line.startswith("Malaysia"):
            current_continent = Malaysia
        elif line.startswith("Australia"):
            current_continent = Australia
        elif line.startswith("Singapore"):
            current_continent = Singapore
        elif line.startswith("England"):
            current_continent = England
        elif line and not line.startswith('--------'):
            line = line.strip().replace(" ", "_")
            current_continent.append(line)


    return continent_lists

    # Print the lists for each continent
    # for continent, countries in continent_lists.items():
    #     print(f"{continent}:\n{'-' * len(continent)}\n{', '.join(countries)}\n")



if __name__ == '__main__':
    main()