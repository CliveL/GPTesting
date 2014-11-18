__author__ = 'Clive'

#functions to check if string matches patterns for primary keys.

import re


def is_vehicle_id(input_id):
    #vehicle ID example: GOL00032
    id_type = re.compile("([a-zA-Z]{3,3}\d{5,5})$")  # three letters, followed by 5 numbers. Allow lowercase letters
    if id_type.match(input_id) is not None:
        result = True
    elif id_type.match(input_id) is None:
        result = False
    else:
        result = False
    return result


def is_part_id(input_id):
    #Part ID example: VAGABC123456789
    id_type = re.compile("([a-zA-Z]{6,6}\d{9,9})$")
    if id_type.match(input_id) is not None:
        result = True
    elif id_type.match(input_id) is None:
        result = False
    else:
        result = False
    return result


def is_listing_id(input_id):
    #listing ID example: AA0000123456789
    id_type = re.compile("([a-zA-Z]{2,2}\d{13,13})$")
    if id_type.match(input_id) is not None:
        result = True
    elif id_type.match(input_id) is None:
        result = False
    else:
        result = False
    return result