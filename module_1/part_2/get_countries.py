
def main():
    # Main menu loop
    # Open the text file and read lines
    with open('../../worldometers_countrylist.txt', 'r') as file:
        lines = file.readlines()

    # Initialize empty lists for each continent
    europe = []
    north_america = []
    asia = []
    south_america = []
    africa = []
    oceania = []

    # Initialize a dictionary to map continents to their respective lists
    continent_lists = {
        "Europe": europe,
        "North America": north_america,
        "Asia": asia,
        "South America": south_america,
        "Africa": africa,
        "Oceania": oceania
    }

    # Flag to identify the current continent
    current_continent = None

    # Iterate through lines and populate continent lists
    for line in lines:
        line = line.strip()
        if line.startswith("Europe"):
            current_continent = europe
        elif line.startswith("North America"):
            current_continent = north_america
        elif line.startswith("Asia"):
            current_continent = asia
        elif line.startswith("South America"):
            current_continent = south_america
        elif line.startswith("Africa"):
            current_continent = africa
        elif line.startswith("Oceania"):
            current_continent = oceania
        elif line and not line.startswith('--------'):
            line = line.strip().replace(" ", "_")
            current_continent.append(line)


    return continent_lists

    # Print the lists for each continent
    # for continent, countries in continent_lists.items():
    #     print(f"{continent}:\n{'-' * len(continent)}\n{', '.join(countries)}\n")



if __name__ == '__main__':
    main()