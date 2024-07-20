#food = ["apple", "coconut", 'banana']
#food.append(True)
#print(food)
#food.extend(["string"])
#print(food)
#food.remove("apple")
#print(food)
#print("coconut" not in food)
#print(food[0:2:2])
#tuple_ = 1, 2, 3, True, "string"
#list_ = [1, 2, 3, True, "string"]
#print(tuple_.__sizeof__())
#print(list_.__sizeof__())
#tuple_ = ([1, 2], 0)
#print(tuple_)
#tuple_[0][0] = 2
#print(tuple_)
#tuple_ = (1, 2) * 3
#print(tuple_)
tuple_ = 1, 2.5, "string"
immutable_var = tuple_
print(immutable_var)
mutable_list = [1, 2.5, "string"]
mutable_list[0] = 200
print(mutable_list)