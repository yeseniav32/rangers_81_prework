foods = ["pizza", "tacos", "dim sum", "sushi"]
#listname[index]
#for PLACEHOLDER in THE_LIST_WE_WANT_TO_LOOK_AT
    # this is a code block
    #this code block
    # will run every item in the list

for food in foods:
    print(food.title())
    print(type(food))
print("Loop is over")

#another way to run this with shorter code and a sentence using the f" function 
for food in foods:
    print(f"I like to eat {food}")

#loop of the index
print(list(range(5)))
print(len(foods)) #len counts the number of items in a list

for index in range(len(foods)):
    print(index)
    print(foods[index])

#more pythonic way to do the above code
print(list(enumerate(foods)))
for tup in enumerate(foods):
    print(tup)
    print(f"My No.1 {index} is {food.title*()}")
