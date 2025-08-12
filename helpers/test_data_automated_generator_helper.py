import itertools

def generate_password_data(password_options, password_character_sets=0):
    '''
    This function generates test cases with combinations of password options

    :param password_options: The options we want to permutate
    :param password_character_sets: The sets of characters to compare the password back to

    :returns: test_data which is a set of data to parameterize for pytest
    '''
    test_data = []
    for length in range(1, len(password_options) + 1):
        list_of_combinations = list(itertools.combinations(password_options, length))
        for item in list_of_combinations:
            character_sets = []
            option_set = ",".join(item)
            for option in item:
                for character_set in password_character_sets:
                    if option in character_set:
                         character_sets.append(character_set[option])
            test_data.append(({"password": option_set}, character_sets))
    return test_data

def generate_country_data(country_data):
    '''
    This function generates test cases with combinations of countries

    :param country_data: The nats we want to have combinations of for thorough testing

    :returns: test_data which is a set of data to parameterize for pytest
    '''
    test_data = []
    #This is hard coded to this range, as there are many combinations. 
    for length in range(1, 2):
        list_of_combinations = list(itertools.combinations(country_data, length))
        for item in list_of_combinations:
            country_set = item
            country_set_string = ",".join(item)
            test_data.append(({"nat": country_set_string}, list(country_set)))
    return test_data

def generate_include_exclude_lists(test_params):
    '''
    This function generates test cases with combinations of parameters to inc and exc

    :param test_params: The parameters to create our combinations

    returns: test_data to paramterize our tests with
    '''
    test_data = []
    #This is hard coded to this range, as there are many combinations. 
    for length in range(1, 2):
        list_of_combinations = list(itertools.combinations(test_params, length))
        for item in list_of_combinations:
            test_param_set = item
            test_param_string = ",".join(item)
            test_data.append(({"inc": test_param_string}, test_param_set, "inc"))
            test_data.append(({"exc": test_param_string}, test_param_set, "exc"))
    return test_data
