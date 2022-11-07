'''
Authored by Daniel Bothwell 
For BlackSky Technical TakeHome
11/2/2022
'''
import pytest
import json
import xml.etree.ElementTree as elementTree
import csv
import yaml

from test_data.testdata import *
from helpers.helpers import *

@pytest.mark.parametrize("params, expected", test_data_200_responses)
def test_200_responses(params, expected):
    '''
    Test to verify successful 200 response codes

    :param params: The params for the url
    :param expected: The expected result
    '''
    response = get_api_response(params)
    actual_status_code = response.status_code
    assert actual_status_code == expected

@pytest.mark.parametrize("params, expected", test_data_requesting_multiple_users)
def test_requesting_multiple_users(params, expected):
    '''
    Test to verify the ability to get multiple users

    :param params: The params for the url
    :param expected: The expected result
    '''
    response = get_api_response(params)
    actual_length = len(response.json()['results'])
    assert actual_length == expected

@pytest.mark.parametrize("params, expected", test_data_specifying_gender)
def test_specifying_gender(params, expected):
    '''
    Test to verify the ability to set gender

    :param params: The params for the url
    :param expected: The expected result
    '''
    response = get_api_response(params)
    gender_values = fetch_all_values_for_key(response.json()['results'], "gender")

    #Using a python shortcut to cut down on duplicate values, so if our final list is longer than 1, we know that both genders are present
    gender_values_set = set(gender_values)
    gender_value_actual = list(gender_values_set)

    assert len(gender_value_actual) <= 1
    assert gender_value_actual[0] in expected

@pytest.mark.parametrize("params, character_lists", test_data_passwords_contents)
def test_passwords_contents(params, character_lists):
    '''
    Test to verify password contents depending on criteria given for password requirments

    :param params: The params for the url
    :param character_lists: The lists of approved characters that need to be present for a valid password
    '''
    password_contains_character_results = []
    response = get_api_response(params)
    password_values = fetch_all_values_for_key(response.json()['results'], "login", "password")
    for character_list in character_lists:
        for password in password_values:
            has_any = any([char in password for char in character_list])
            password_contains_character_results.append({"password": password, "result": has_any})
    assert check_results(password_contains_character_results)

@pytest.mark.parametrize("params, length", test_data_passwords_length)
def test_passwords_length(params, length):
    '''
    Test to verify password lengths

    :param params: The params for the url
    :params length: The min and max of the length we expect
    '''
    password_length_results = []
    response = get_api_response(params)
    password_values = fetch_all_values_for_key(response.json()['results'], "login", "password")
    for password in password_values:
        password_length_results.append({"password": password, "result": len(password) in range(length[0], length[1])})
    assert check_results(password_length_results)

@pytest.mark.parametrize("params_1, params_2, expected", test_data_seed)
def test_seed(params_1, params_2, expected):
    '''
    Test the seed parameter

    :param params_1: The first param to get a seed result
    :param params_2: The second param to get another seed result
    :param expected: The expected result
    '''
    first_response = get_api_response(params_1)
    second_response = get_api_response(params_2)
    assert (first_response.json() == second_response.json()) == expected

@pytest.mark.parametrize("params, expected_format, expected", test_data_format)
def test_format(params, expected_format, expected):
    '''
    Test the format of the data

    :param params: The params for the url
    :param expected_format: The expected format, i.e. csv, json, etc...
    :param expected: The response we expect back
    '''
    response = get_api_response(params).text
    valid_response = False
    if expected_format == "json":
        try:
            json.loads(response)
            valid_response = True
        except:
            valid_response = False
    if expected_format == "csv":
        try:
            contents = csv.reader(response.splitlines())
            for row in contents: 
                if len(row) == 0:
                    valid_response = False
                else:
                    valid_response = True
        except: 
            valid_response = False
    if expected_format == "xml":
        try: 
            elementTree.fromstring(response)
            valid_response = True
        except:
            valid_response = False
    if expected_format == "yaml":
        try:
            yaml.dump(yaml.safe_load(response))
            valid_response = True
        except:
            valid_response = False
    
    assert valid_response == expected


@pytest.mark.parametrize("params, country_set", test_data_country)
def test_country(params, country_set):
    '''
    Test the count for nat that we set

    :param params: The params for the url
    :param country_set: The set of countries we should see in our data set from the response
    '''
    response_contains_nat_results = []
    response = get_api_response(params)
    nat_values = fetch_all_values_for_key(response.json()['results'], "nat")
    for nat in nat_values:
            if nat in country_set:
                nat_result = True
            else:
                nat_result = False
            response_contains_nat_results.append({"nat": nat, "result": nat_result})
    assert check_results(response_contains_nat_results)

@pytest.mark.parametrize("params_1, params_2, expected", test_data_pagination)
def test_pagination(params_1, params_2, expected):
    '''
    Test the pagination of the api

    :param params_1: The first param to get a pagination result
    :param params_2: The second param to get another pagination result
    :param expected: The value we expect for our assert
    '''
    first_response = get_api_response(params_1)
    second_response = get_api_response(params_2)
    assert (first_response.text == second_response.text) == expected

@pytest.mark.parametrize("params, list, type", test_data_params)
def test_param_inc_exc(params, list, type):
    '''
    Test the combination of parameters we exclude and include

    :param params: The parameters to modify the url with
    :param list: The list of parameters we modified the url with for comparison
    :param type: The type of action, include or exclude
    '''
    key_list = []
    param_result_list = []
    response = get_api_response(params)
    response_values = response.json()["results"]
    for value in response_values:
        for key in value.keys():
            key_list.append(key)
    if type == "inc":
        print(key_list)
        has_all = all([key in key_list for key in list])
        param_result_list.append({"key_list": key_list, "result": has_all})
    if type == "exc":
        does_not_have = not any(([key in key_list for key in list]))
        param_result_list.append({"key_list": key_list, "result": does_not_have})
    assert check_results(param_result_list)