planet_list = ["Mercury", "Mars"]
last_two = ["Uranas", "Neptune"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.insert(1,"Venus")
planet_list.insert(2,"Earth")

last_two.append("Pluto")

planet_list.extend(last_two)

del planet_list[8];
print(planet_list)

print(planet_list[0:4])
