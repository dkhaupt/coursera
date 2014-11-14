#file with info
FILENAME = 'restaurants_small.txt'

def recommend(file, price, cuisines_list):
    #accept a filename, desired price, and list of desired cuisines and output restaurants matching and their ratings

    #read file and build data structures
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    #look up list of names for desired price
    names_matching_price = price_to_names[price]

    #create list of restaurants with desired cuisine
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    #sort list by rating
    result = build_rating_list(name_to_rating, names_final)

    #return sorted list
    return result[::-1]

def read_restaurants(file):
    #return dict {name: rating}
    #return dict {price: list of names}
    #return dict {cuisine: list of names}

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    f = open(file, 'r')
    for line in f:
        name = line.rstrip()
        rating = f.readline().rstrip()
        price = f.readline().rstrip()
        cuisines = f.readline().rstrip()

        name_to_rating[name] = int(rating[:-1])
        price_to_names[price].append(name)
        cuisines = cuisines.split(', ')
        for cuisine in cuisines:
            if cuisine not in cuisine_to_names:
                cuisine_to_names[cuisine] = [name]
            else:
                cuisine_to_names[cuisine].append(name)
        
        f.readline() #space between restaurants   
    f.close()
        
    return name_to_rating, price_to_names, cuisine_to_names 

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    #return list of restaurants from provided list which match desired cuisine(s)
    cuisines_list = cuisines_list.split(', ')
    names_final = []

    for cuisine in cuisines_list:
        for restaurant in cuisine_to_names[cuisine]:
            if restaurant in names_matching_price and restaurant not in names_final:
                names_final.append(restaurant)

    return names_final

def build_rating_list(name_to_rating, names_final):
    #take in list of restaurants matching price and cuisine, return that list sorted by rating

    result = []

    for name in names_final:
        result.append([name_to_rating[name], name])

    return sorted(result)

print(recommend(FILENAME, '$', 'Thai, Chinese'))
