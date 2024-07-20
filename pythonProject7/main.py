my_dict = {"Denis": 2006, "Sasha": 2009, "Anton": 2012}
my_dict["Alex"] = 2007
print(my_dict["Alex"])
print(my_dict["Sasha"])
my_dict.update({"Ivan": 1998,
                "Dima": 2000})
print(my_dict)
del my_dict["Denis"]
print(my_dict)
my_set = {1, 2, 3, 4, 5, "String", True, (1, 2, 3)}
print(my_set)
my_set.add(6)
my_set.add(7)
print(my_set)
my_set.discard(3)
print(my_set)