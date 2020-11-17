import re
from exceptions import InvalidCoordinateException

coords = re.compile("([0-9]+[\.\d+]*)([°'\"])")

factor = {
    "°": 1,
    "'": 60,
    "\"": 3600
}


def is_decimal(input):
    try:
        float(input)
    except ValueError:
        return False
    else:
        return True
'''
def convert_coords_to_decimal(input):
    decimal = 0
    coords_list = re.findall(coords, input)
    for n in coords_list:
        decimal += (float(n[0]) / factor[n[1]])
    return decimal
'''
def convert_coords_to_decimals(input):
    axis_check = [False, False]
    coordinates = [0.0, 0.0]
    for k in input:
        decimal = 0
        write_index = 0
        if "E" in k or "W" in k:
            if axis_check[0]:
                continue
            else:
                axis_check[0] = True
        if "N" in k or "Z" in k:
            if axis_check[1]:
                continue
            else:
                axis_check[1] = True
                write_index = 1
        coords_list = re.findall(coords, k)
        for n in coords_list:
            decimal += (float(n[0]) / factor[n[1]])
        coordinates[write_index] = decimal
    for n in axis_check:
        if not n:
            raise InvalidCoordinateException("Invalid coordinate(s) found!")
    return coordinates

def is_in_boundaries(bounds, coordX, coordY, scale=5.0):
    scale_factor = 0.0001
    modifier = scale * scale_factor
    # k-file: (left, right, top, bottom)
    # if ((bounds[0] + modifier) < coordX and (bounds[1] - modifier) > coordX and (bounds[2] - modifier) > coordY and (bounds[3] + modifier) < coordY):
    if bounds[0] < coordX < bounds[1] and bounds[2] > coordY > bounds[3]:
        return True
    return False
