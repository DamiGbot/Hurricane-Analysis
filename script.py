# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
updated_damage = []
def getting_damages():
    for damage in damages:
        if damage[0] == "D":
            updated_damage.append("Damages not recorded")
        elif damage[-1] == "M":
            updated_damage.append(float(damage[:-1]) * 1000000)
        elif damage[-1] == "B":
            updated_damage.append(float(damage[:-1]) * 1000000000)

    return updated_damage

getting_damages()

# write your construct hurricane dictionary function here:
hurricane = {}
hurricane_year = {}

def update_hurricane_dict():
    for name,month,year,max_wind,area_affected,damage,death in zip(names, months, years, max_sustained_winds, areas_affected, updated_damage, deaths):
        personal_data = {
            "Name" : name, 
            "Month": month, 
            "Year": year, 
            "Max Sustained Wind": max_wind, 
            "Areas Affected": area_affected, 
            "Damage": damage, 
            "Deaths": death,
        }
        hurricane[name] = {}
        hurricane[name].update(personal_data)
        hurricane_year[year] = {}
        hurricane_year[year].update(personal_data)
    return hurricane , hurricane_year

hurricane_data_by_name, hurricane_data_by_year = update_hurricane_dict()

# write your construct hurricane by year dictionary function here:
sorted_hurricane_data_by_year = {}
for key in sorted(hurricane_data_by_year):
    sorted_hurricane_data_by_year[key] = hurricane_data_by_year[key]

# write your count affected areas function here:
updated_areas_affected = {}
def getting_updated_areas_affected():
    for lst in areas_affected:
        for word in lst:
            if not word in updated_areas_affected:
                updated_areas_affected[word] = 1
            else:
                updated_areas_affected[word] += 1
    return updated_areas_affected

getting_updated_areas_affected()

# write your find most affected area function here:
def getting_most_affected_area():
    most_affected_area = 0
    for key,value in updated_areas_affected.items():
        if value > most_affected_area:
            most_affected_area = value
            result = key
    return "The most affected area is {} affected {} times.".format(result, most_affected_area)

getting_most_affected_area()

# write your greatest number of deaths function here:
def most_number_of_deaths(hurricane):
    highest_number_deaths = 0
    for name in hurricane:
        for key,value in hurricane[name].items():
            if key == "Deaths":
                if hurricane[name][key] > highest_number_deaths:
                    highest_number_deaths = hurricane[name][key]
                    result = hurricane[name]["Name"]
    return "{} caused the highest death ({} deaths)".format(result, highest_number_deaths)

most_number_of_deaths(hurricane_data_by_name)

# write your catgeorize by mortality function here:
mortality_rate = {}
mortality_rate.update({0: [], 1: [], 2: [], 3: [], 4: [], 5: []})
def calculate_mortality_rate(hurricane):
    for name in hurricane:
        for key,value in hurricane[name].items():
            if key == "Deaths":
                if hurricane[name][key] <= 0:
                    mortality_rate[0].append(hurricane[name]["Name"])
                elif hurricane[name][key] > 0 and hurricane[name][key] <= 100:
                    mortality_rate[1].append(hurricane[name]["Name"])
                elif hurricane[name][key] > 100 and hurricane[name][key] <= 500:
                    mortality_rate[2].append(hurricane[name]["Name"])
                elif hurricane[name][key] > 500 and hurricane[name][key] <= 1000:
                    mortality_rate[3].append(hurricane[name]["Name"])
                elif hurricane[name][key] > 1000 and hurricane[name][key] <= 10000:
                    mortality_rate[4].append(hurricane[name]["Name"])
                else:
                    mortality_rate[5].append(hurricane[name]["Name"])

    return mortality_rate

calculate_mortality_rate(hurricane_data_by_name)

# write your greatest damage function here:
def most_number_of_damages(hurricane, lst):
    highest_number_damages = 0
    damage_cost = ""
    most_damages = ""
    for name in hurricane:
        for key,value in hurricane[name].items():
            if key == "Damage":
                if type(hurricane[name][key]) == float:
                    if hurricane[name][key] > highest_number_damages:
                        highest_number_damages = hurricane[name][key]
                        most_damages = hurricane[name]["Name"]

    # return highest_number_damages
    return "{} caused the highest damages {}".format(most_damages, highest_number_damages)

most_number_of_damages(hurricane_data_by_name, damages)

# write your catgeorize by damage function here:
damage_scale = {}
damage_scale.update({0: [], 1: [], 2: [], 3: [], 4: [], 5: []})
def damage_level(hurricane):
    for name in hurricane:
        for key,value in hurricane[name].items():
            if key == "Damage":
                if type(hurricane[name][key]) == float:
                    if hurricane[name][key] <= 0:
                        damage_scale[0].append(hurricane[name]["Name"])
                    elif hurricane[name][key] > 0 and hurricane[name][key] <= 100000000:
                        damage_scale[1].append(hurricane[name]["Name"])
                    elif hurricane[name][key] > 100000000 and hurricane[name][key] <= 1000000000:
                        damage_scale[2].append(hurricane[name]["Name"])
                    elif hurricane[name][key] > 1000000000 and hurricane[name][key] <= 10000000000:
                        damage_scale[3].append(hurricane[name]["Name"])
                    elif hurricane[name][key] > 10000000000 and hurricane[name][key] <= 50000000000:
                        damage_scale[4].append(hurricane[name]["Name"])
                    else:
                        damage_scale[5].append(hurricane[name]["Name"])
    return damage_scale

damage_level(hurricane_data_by_name)

