programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
programming_dictionary["Loop"] = "Doing an action over and over"
programming_dictionary["Bug"] = "An error in a program that makes the program run unexpected."

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

travel_log = [
    {
        "Country": "France",
        "vities_visited":["Paris","Lille"],
        "total_visits": 12
    },
    {"Country": "Germany",
    "vities_visited":["Berlin","Hamburg"],
    "total_visits": 5
    }
]
print(travel_log[0])

