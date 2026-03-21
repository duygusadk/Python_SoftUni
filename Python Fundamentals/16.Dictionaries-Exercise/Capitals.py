countries = input().split(", ")
capitals = input().split(", ")

county_capital = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in county_capital.items():
    print(f"{country} -> {capital}")
