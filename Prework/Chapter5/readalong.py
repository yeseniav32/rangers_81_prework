cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You just earned 5 points!")

number = 8
if number <= 8:
    print("Number is greater than 8")
else:
    print("Number is less than 8")

name = "destiny's child"
if name == "destiny's child":
    print("say my name, say my name", end=" ")
print("if no one is around you", end=" ")
if name:
    print("say baby i love you", end=" ")
else:
    print("if you ain't runnin' game", end=" ")