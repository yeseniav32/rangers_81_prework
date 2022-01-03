#Question 1 - Write a function to print "Hello USERNAME"

def hello_name(user_name):
    print("Hello " + user_name.upper())

#hello_name("Yesenia")

#Question 2 - Print the first odd numbers between 1 and 100

def first_odds():
    for num in range(1,100):
        if num % 2 != 0:
            print(num)

#first_odds()

#Question 3 - Write a funtion thath returns the max number in a given list

def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list([175,20,35,4]))

#Question 4 - Write a funtion to return if the given year is a leap year

def is_leap_year(a_year):
    if a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 ==0:
        return True
    else:
        return False

print(is_leap_year(2024))
print(is_leap_year(2022))

#Question 5 - Write a funtion to check if the numbers in a given list are consecutive

def is_consecutive(a_list):
    #create a checklist to compare our input list to
    check_list = list(range(min(a_list), max(a_list)+1))

    if a_list == check_list:
        print("\nNumbers in list are consecutive :)")
    else:
        print("\nNumbers are not consecutive :(")

is_consecutive([1,2,3,4,5])
is_consecutive([1,3,4,5,2])