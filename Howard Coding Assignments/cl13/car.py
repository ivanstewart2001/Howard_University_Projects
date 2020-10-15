# Take in user input in pairs of city names and miles from previous cities.
# When the user types "done" for the city name, prompt the user for the range of their car.
# Finally, print out the furthest city in the route that the user can make it to before recharging.

def adding_lists(*args):
    total = 0
    for i in args:
        total += int(i)
    return total

def calculate(city : list, miles: list, range_list: list): 
    miles_sum = sum(int(i) for i in miles)
    range_str = ''
    for i in range_list:
        range_str += str(i)

    if int(range_str) < int(miles[0]):
        return "You cannot make it to your first stop."

    elif int(range_str) < miles_sum:
        if int(miles[0]) <= int(range_str) < adding_lists(miles[0], miles[1]):
            return "You can make it to " + str(city[0]) + " before recharging."
        elif int(miles[0]) < int(range_str) < adding_lists(miles[0], miles[1], miles[2]):
            return "You can make it to " + str(city[1]) + " before recharging."
        elif adding_lists(miles[0], miles[1]) < int(range_str) < adding_lists(miles[0], miles[1], miles[2], miles[3]):
            return "You can make it to " + str(city[2]) + " before recharging."
        elif adding_lists(miles[0], miles[1], miles[2]) < int(range_str) < adding_lists(miles[0], miles[1], miles[2], miles[3], miles[4]):
            return "You can make it to " + str(city[3]) + " before recharging."

    elif int(range_str) >= miles_sum:
       return "You can make it all the way to your destination."

print(calculate(['columbus', 'pittsburg', 'cincinnati'], [23456,2345,2345], [1]))

# def run():
#     getting_cities = True
#     city_list_1 = []
#     mile_list_1 = []
#     range_list_1 = []
#     while getting_cities:
#         city = input("City: ")
#         city_list_1.append(city)
#         if city == "done":
#             getting_cities = False
#             range_input = input("Range: ")
#             range_list_1.append(range_input)
#             x = calculate(city_list_1, mile_list_1, range_list_1)
#             print(x)
#         else:
#             miles = input("Miles: ")
#             mile_list_1.append(miles)

# if __name__ == "__main__":
#     run()