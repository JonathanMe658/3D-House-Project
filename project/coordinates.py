import re

coords = re.compile("([0-9]+[\.\d+]*)([°'\"])")

factor = {
    "°" : 1,
    "'" : 60,
    "\"" : 3600
    }

def convert_coords_to_decimal(input):
    decimal = 0
    coords_list = re.findall(coords, input)
    for n in coords_list:
        decimal += (float(n[0]) / factor[n[1]])
    return decimal

def is_in_boundaries(bounds, coordX, coordY, scale=5.0):
    scale_factor = 0.0001
    modifier = scale * scale_factor
    if ((bounds[0] + modifier) < coordX and (bounds[1] - modifier) > coordX and (bounds[2] + modifier) < coordY and (bounds[3] + modifier) > coordY):
        return True
    return False
