def get_coldest_city(cities):
    coldest_city = {}

    for city in cities:
        if coldest_city:
            if city["temp"] <= coldest_city["temp"]:
                coldest_city["name"] = city["name"]
                coldest_city["temp"] = city["temp"]
                coldest_city["weather"] = city["weather"]
                coldest_city["humidity"] = city["humidity"]
        else:
            coldest_city["name"] = city["name"]
            coldest_city["temp"] = city["temp"]
            coldest_city["weather"] = city["weather"]
            coldest_city["humidity"] = city["humidity"]

    return coldest_city