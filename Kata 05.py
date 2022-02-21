from math import ceil, floor

dis_earth = 149597870 #km
dis_Jupyter = 778547200 #km

dis_km_btw__earth_jupyter = abs(dis_Jupyter - dis_earth);
dis_miles_btw_earth_jupyter = ceil(0.621 * dis_km_btw__earth_jupyter)

print(f"Distance in km btw Earth-Jupyter = {dis_km_btw__earth_jupyter}")
print(f"Distance in miles btw Earth-Jupyter = {dis_miles_btw_earth_jupyter}")


planet1 = int(input("Distance btw planet one and sun --> "))
planet2 = int(input("Distance btw planet two and sun --> "))


km_distance_btw = abs(planet1 - planet2)
mi_distance_btw = km_distance_btw * 0.621

print(km_distance_btw + " km.")
print(mi_distance_btw + " mi.")

