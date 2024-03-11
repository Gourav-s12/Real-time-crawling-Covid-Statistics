import option_new_death
import option_active_case
import option_new_case_recovered
import option_new_case
import webpage_download_country
import get_countries
import marge_output

countries = {}
def main(country):
    # Main menu loop
    countries = get_countries.main()
    # webpage_download_country.main(countries['Asia'][11])
    
    # Iterate through continents
    for continent, country_list in countries.items():
        # Iterate through countries in each continent
        if country in country_list:
            # Call the specified functions for each country
            webpage_download_country.main(country)
            option_active_case.main(country)
            option_new_death.main(country)
            option_new_case_recovered.main(country)
            option_new_case.main(country)
            make_File(country)
            
            print(f"detail fetched for {country}")
            return
    
    print("Entered country is not on our watch list")

def make_File(country):
    marge_output.main('new_recovered_case_date', country+'_new_recovered')
    marge_output.main('daily_death_date', country+'_daily_death')
    marge_output.main('active_case_date', country+'_active_case')
    marge_output.main('new_recovered_case_date', country+'_new_case')

if __name__ == '__main__':
    main("India")