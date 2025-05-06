european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]
# Create an empty dictionary: european_cities_info
european_cities_info={}
# Loop over the european_cities and unpack each tuple
for k,v in european_cities:
 european_cities_info[k]=v
print(european_cities_info)
# Print dictionary with the format City --> [Population, Dish, Landmark]
for city,[Population,Dish,Landmark]in european_cities:
    european_cities_info[city]= [Population,Dish,Landmark]
print([Population,Dish,Landmark]) 
# Sort the european_cities_info dictionary alphabetically by city (use sorted)
x=dict(sorted(european_cities_info.items()))
for city,[Population,Dish,Landmark] in european_cities_info:
     print(f'{city}.........{[Population,Dish,Landmark]}')
# Safely print the 'Berlin' info from the european_cities_info dictionary
x=european_cities_info.get("Berlin")
print(f'infor for Berlin:{x}')
# Safely print the type of 'London' from the european_cities_info dictionary
if "London" in european_cities_info:
 print(f" The type of London :{type("London")}")
# Safely print 'Barcelona' from the european_cities_info dictionary or 'Not Found' 
y=european_cities_info.get("Barcelona")
if "'Barcelona" in european_cities_info:
 print(f'information for Barcelona:{x}')
else:
 print("not found")
# Add new city ("Rome", [2870500, "Pasta", "Colosseum"])
european_cities_info["Rome"]=[2870500, "Pasta", "Colosseum"]
print(european_cities_info)
# Remove "Madrid" from european_cities_info
european_cities_info.pop("Madrid")
print(european_cities_info)
# Check to see if Amsterdam is in european_cities_info and print whether it is there or not
if "Amsterdam" in european_cities_info:
 print("AMSTERDAM ist da")
else:
    print("nicht da")
# Bonus: Create a dictionary from two lists:
# Use the functions dict() and zip()
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"] 
countries = ["Italy", "Germany", "Spain", "USA"]
dishes_countries_dictionary=dict(zip(countries,dishes))
print(dishes_countries_dictionary)