city = ["Mumbai", "Pune", "Gaya", "Patna", "Kolkata", "Gurgon", "Bhopal","Indore"]

print(f"First 4 City:",city[:4])
print(f"Last 4 City:",city[4:])
city.append("Orissa")
city.pop(0)

print(f"Final City:", city)

city_tuple = tuple(city)
print("Tuple :", city_tuple)