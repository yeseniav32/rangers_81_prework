my_list = []
my_list = list()
print(type(my_list))

#index     0, 1, 2,  3,    4
numbers = [2, 4, 10, 12.4, 0]#this is also a comment
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print(numbers[1]* 2.5)

print(numbers[3])
print(type(numbers[3]))

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods[1])
print(type(foods[1]))

x = 12
y = 15.5
z = "Z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_fav_num = random_list[2]
print(my_fav_num)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append("cheeseburger")
print(foods)

#foods = foods.append("cheeseburger") DOES NOT WORK TO ADD TO THE LIST

#HOW TO INSERT A VARIABLE INTO A LIST
foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.insert(0, "pho")
print(foods)

#HOW TO REMOVE A VARIABLE FROM A LIST
foods.remove("pho")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append('pizza')
print(foods)
foods.remove("pizza")
print(foods)
foods.remove("pizza")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods)
del foods[1]
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.pop())
print(foods)

#Method of the list class called .sort
#built-in function called sorted()

#.sort() is IN PLACE
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

#Sorted is out of place
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(sorted(foods))
print(foods)
foods = sorted(foods)
print(foods)
foods = sorted(foods, reverse=True)
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.reverse()
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods(0+1)