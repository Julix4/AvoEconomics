# Listas para la clasificación de location
newyork = ["NewYork", "Albany"]
florida = ["MiamiFtLauderdale", "Orlando"]
texas = ["Houston", "DallasFtWorth"]
louisiana = ["NewOrleansMobile", "Atlanta"]
california = ["SanDiego", "SanFrancisco", "Sacramento"]

otros = ["SouthCarolina", "StLouis", "CincinnatiDayton", "GrandRapids",
         "Indianapolis", "Columbus", "Detroit", "Chicago", "Charlotte",
         "Providence", "Boston", "BuffaloRochester", "NorthernNewEngland",
         "HartfordSpringfield", "HarrisburgScranton", "NewYork", "Pittsburgh",
         "Philadelphia", "Spokane", "Boise", "Seattle", "Portland", "Denver",
         "WestTexNewMexico", "LasVegas", "PhoenixTucson", "Louisville",
         "RichmondNorfolk", "RaleighGreensboro", "Roanoke", "BaltimoreWashington",
         "Nashville", "Tampa", "LosAngeles", "Jacksonville"]

# Funcion de clasificación


def get_group_location(location):
    if location in newyork:
        return 'newyork'
    elif location in florida:
        return 'florida'
    elif location in texas:
        return 'texas'
    elif location in louisiana:
        return 'louisiana'
    elif location in california:
        return 'california'
    elif location == 'TotalUS':
        return 'TotalUS'
    else:
        return 'otros'
