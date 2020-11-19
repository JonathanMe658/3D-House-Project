import re
from exceptions import InvalidCoordinateException
#TODO: add room for spaces in the regex 51° 12' 23" [\s]*
coords = re.compile(r"([0-9]+[\.\d+]*)([°'\"])")

factor = {
    "°": 1,
    "'": 60,
    "\"": 3600
}


# Check if contents of string input are a number
def is_decimal(input: str) -> bool:
    try:
        float(input)
    except ValueError:
        return False
    else:
        return True


# Convert input string DMS coordinates to decimal coordinates
def convert_coords_to_decimals(input: list) -> list:
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


# Check if float coordinates are in the bounding box of the k-file
def is_in_boundaries(bounds: tuple, coordX: float, coordY: float, scale: float = 8.0) -> bool:
    # k-file: (left, right, top, bottom)
    if bounds[0] < coordX < bounds[1] and bounds[2] > coordY > bounds[3]:
        return True
    return False
