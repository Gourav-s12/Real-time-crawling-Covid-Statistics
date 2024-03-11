import sys 

country = None 
date = None 
cases = 0 
Country = sys.argv[1]
Country = Country.strip()
my_dict = {}


for line in sys.stdin: 
    date, country, cases = line.strip().split(" ")
    country = country.strip()
    cases = int(cases)
    if country in my_dict:
        change = cases - my_dict[country]
        if my_dict[country] == 0 : 
            my_dict[country] = 1
        my_dict[country] = (100*(change)/my_dict[country])
    else : 
        my_dict[country] = cases

print(f"{'Decrease' if my_dict[Country]<0 else 'Increase'} in {Country} : {my_dict[Country]}%")

diff = sys.maxsize
similar = None
for k, v in my_dict.items(): 
    if k != Country and abs(v - my_dict[Country]) < diff : 
        similar = k 
        diff = abs(v-my_dict[Country])
print(f"Closest Country with Similar Statistics is {similar} with {my_dict[similar]}%")
