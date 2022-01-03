alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0 = {'color': 'green', 'points': 5}
print(type(alien_0['color']))
print(type(alien_0['points']))

my_dict = {
    "name": "Troy Aikman",
    "position":"QB",
    "team": "Dallas Cowboys",
    "age": 54,
    "weight": 220.,
    "superbowls": ["XXVII", "XXVIII", "XXX"],
    "awards":{
            "super bowl_mvp": "XXVII",
            "probowl":[1991, 1992, 1993, 1994, 1995, 1996],
            "man_of_the_year":1997
        }
    }
for key in my_dict:
    if key>"position":
        print(key, end=" ")

for key, value in my_dict.items():
    if value== 54:
        print("Old", end=" ")
    if value== "age":
        print("54", end=" ")

my_dict["awards"]["probowl"].reverse()
print(my_dict["awards"]["probowl"].pop(2))

print(my_dict.get("awards","age")["probowl"][len(my_dict["position"])])
    
