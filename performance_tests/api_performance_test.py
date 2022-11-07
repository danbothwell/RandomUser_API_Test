'''
Authored by Daniel Bothwell 
For BlackSky Technical TakeHome
11/2/2022
'''
import pytest
import requests

from conftest import base_url
from test_data.testdata import *
from helpers.helpers import *

@pytest.mark.parametrize("params, expected", test_data_200_responses)
def test_200_responses_times(params, expected):
    '''
    This test case tests the response times of various successful calls. 

    :param params: The parameters for the url to make the api call
    :param expected: The expected outcome, not currently used

    :assert: This test checks that the response time is less than 500 ms
    '''
    response = get_api_response(params)
    response_time = response.elapsed.total_seconds()
    assert response_time < .5