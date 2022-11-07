'''
Authored by Daniel Bothwell 
For BlackSky Technical TakeHome
11/2/2022
'''
from helpers.test_data_automated_generator_helper import *
import datetime

'''
This is our test data to verify all 200 responses we would expect, this does not verify the data itself. 
Not all permutations are here, simply a nice set of cases to verify basic functionality of each of the parameter options
'''
test_data_200_responses = [
    ({}, 200),
    ({"results": 1}, 200),
    ({"gender": "male"}, 200),
    ({"password": "password=upper,lower,1-16"}, 200),
    ({"seed": "test"}, 200),
    ({"format": "csv"}, 200),
    ({"nat": "gb"}, 200), 
    ({"page": "3"}, 200),
    ({"inc": "gender"}, 200),
    ({"exc": "gender"}, 200)
]

'''
This is our test data to test our results parameter. 
First check 1 and 5000, the expected boundaries.
Then check 0, -1, and 5001 to see that there is a default that the api returns to.
Then check a float, such as 5000.0001.
Then check a string, such as "Bad Data Test".
Then check a date, currently using now()
'''
test_data_requesting_multiple_users = [
    ({"results": 1}, 1),
    ({"results": 5000}, 5000),
    ({"results": -1}, 1),
    ({"results": 5001}, 1), 
    ({"results": 5000.0001}, 1),
    ({"results": "Bad Data Test"}, 1),
    ({"results": datetime.datetime.now()}, 1),
]

'''
This is our gender test. 
We check male, female.
Then we check for multiple results of male and female. 
Then we check bad test data which will return a random response.
We check a bad string, a number, and a date format. 
'''
test_data_specifying_gender = [
    ({"gender": "female"}, ["female"]),
    ({"gender": "male"}, ["male"]),
    ({"gender": "female", "results": 10}, ["female"]),
    ({"gender": "male", "results": 10}, ["male"]),
    ({"gender": "Bad Data Test"}, ["female", "male"]),
    ({"gender": 1}, ["female", "male"]),
    ({"gender": datetime.datetime.now()}, ["female", "male"]),
]

'''
These are our password options we use to create our test data in the helper function. 
'''
password_options = [
    "upper", 
    "lower", 
    "special",
    "number"]
password_character_sets = [
    {"upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"},
    {"lower": "abcdefghijklmnopqrstuvwxyz"},
    {"special": "!\"#$%&\'()*+,- ./:;<=>?@[\]^_`{|}~"},
    {"number": "0123456789"}
]
test_data_passwords_contents = generate_password_data(password_options, password_character_sets)


'''
The password length was a seperate test scenario to keep 1 assert per test. 
Check default
Check minimum
Check a normal set
check a bad input (defaults back to 8, 64)
'''
test_data_passwords_length = [
    ({"password": "upper,lower"}, [8, 64]),
    ({"password": "upper,lower,1"}, [0, 2]),
    ({"password": "upper,lower,1-8"}, [1, 9]),
    ({"password": "upper,lower,Bad Data Test-8"}, [8, 64])
]

'''
Test that a seed test returns the value we expect
Test 2 different seeds
'''
test_data_seed = [
    ({"seed": "test"}, {"seed": "test"}, True),
    ({"seed": "test"}, {"seed": "test1"}, False),
]

'''
This checks for various format options.
'''
test_data_format = [
    ({"format": "json"}, "json", True),
    ({"format": "csv"}, "csv", True),
    ({"format": "xml"}, "xml", True),
    ({"format": "yaml"}, "yaml", True),
]

'''
This is our data to generate the combinations of country data we want to test. 
'''
country_data = ["AU", "BR", "CA", "CH", "DE", "DK", "ES", "FI", "FR", "GB", "IE", "IN", "IR", "MX", "NL", "NO", "NZ", "RS", "TR", "UA", "US"]
test_data_country = generate_country_data(country_data)

'''
Test pagination.
First check that it works as expected with a happy path.
Then check with different pages.
Then check with different seeds.
'''
test_data_pagination = [
    ({"page": 3, "results": 10, "seed": "test"}, {"page": 3, "results": 10, "seed": "test"}, True),
    ({"page": 2, "results": 10, "seed": "test"}, {"page": 3, "results": 10, "seed": "test"}, False),
    ({"page": 3, "results": 10, "seed": "test"}, {"page": 3, "results": 10, "seed": "test1"}, False)
]

'''
The last data set is our combinations of params to include and exclude
'''
test_params = [
    "gender",
    "name",
    "location",
    "email",
    "login",
    "registered",
    "dob",
    "phone",
    "cell",
    "id",
    "picture",
    "nat"
]
test_data_params = generate_include_exclude_lists(test_params)