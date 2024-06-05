def city_country(City, Country, population=''):
    if population:
        result = f"{City} {Country} -population {population}"
        return result
    else:
        result = f"{City} {Country}"
        return result



    