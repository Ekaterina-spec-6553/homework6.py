my_dict = {"Kate": 1999, "Michael": 1994, "Max": 1995, "Egor": 2003}
print(my_dict)
print(my_dict.get("Max"))
print(my_dict.get("Yana"))
my_dict.update({"Nataly": 1978, "Vladimir": 1997})
m = my_dict.pop("Michael")
print(m)
print(my_dict)

my_set = {55, 55, 55, "Reebook", "BMW", "Reebook", 36.6}
print(my_set)
my_set.add((1, 2, 3))
my_set.add("Apple")
my_set.discard("Reebook")
print(my_set)