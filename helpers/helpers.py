'''
Authored by Daniel Bothwell 
For BlackSky Technical TakeHome
11/2/2022
'''
import requests

from conftest import *

def get_api_response(params):
    '''
    This helper fucntion gets the api response

    :param params: The parameters to modify the base url

    :returns: The response of the request
    '''
    response = requests.get(base_url, params=params)
    return response

def fetch_all_values_for_key(json, key_to_search, second_level_key_to_search=None):
    '''
    This function fetches all values for keys

    :param json: The json object to parse
    :param key_to_search: The first key to search by
    :param second_level_key_to_search: Default none, allows for another layer of searching by key

    :returns: A list of values
    '''
    values = []
    for dictionary in json:
        if key_to_search in dictionary:
            dictionary_found = dictionary[key_to_search]
            if second_level_key_to_search:
                if second_level_key_to_search in dictionary_found:
                    values.append(dictionary_found[second_level_key_to_search])
            else:
                 values.append(dictionary[key_to_search])
    return values

def check_results(results_list):
    '''
    This helper function checks the results for success

    :param results_list: A list of results, for historical tracking, can be saved to a database
    
    :returns: True or False, for an assert later
    '''
    for result in results_list:
        if result["result"] == False:
            return False
    return True