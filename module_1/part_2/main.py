import option_new_death
import option_active_case
import option_new_case_recovered
import option_new_case
import webpage_download_country
import get_countries
import main_single_country

countries = {}
def main():
    # Main menu loop
    countries = get_countries.main()
    print(countries)
    # webpage_download_country.main(countries['Asia'][11])
    
    # Iterate through continents
    for continent, country_list in countries.items():
        # Iterate through countries in each continent
        for country in country_list:
            print(country)
            # Call the specified functions for each country
            webpage_download_country.main(country)
            option_active_case.main(country)
            option_new_death.main(country)
            option_new_case_recovered.main(country)
            option_new_case.main(country)


if __name__ == '__main__':
    main()