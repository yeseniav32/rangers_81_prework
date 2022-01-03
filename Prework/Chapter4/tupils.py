#reassinging strings
my_string = "Steve"
my_string = my_string + " smells like teen spririt"
print(my_string)

#declaring tuples
my_tup = 1, 2
print(type(my_tup))
my_tup = (1, 2)
print(type(my_tup))
print(my_tup)

#you cannot add to a tuple but rather add strings

for num in my_tup:
    print(num)

#adding to tuples
my_tup = my_tup +(3, 4)
print(my_tup)

#slicing
my_ring = "Hey Guys Lets Learn Python"
my_list = ["pizza", "tacos", "dim sum", "sushi"]
print(my_ring[4:7]) #this code brings out the word guy as it is looking for the 4th charactor to the 7th

#Quiz for chapters #3&4
deck = ["pikachu", "mew", "mewtwo", "chizard"]
deck = deck.pop()
print(deck)

my_idea = ["it's", "peanut butter", "jelly", "time"]
new_word=''
for word in my_idea:
    new_word += word + " "
print(new_word)

my_num = [1, 3.0, ["a","b", ["A", "B", "C"], "d"], "JOhn"]
print(my_num[2][2][0])

my_food = ["chicken wing", "chicken wing", "sauce"]
for food in my_food:
    if food == "chicken wing":
        break
    print(food, end= " ")