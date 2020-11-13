import re

input = "51.0°45.0'45.0\""

output = re.findall("([0-9]+[\.\d+]+)([°'\"])", input)
print(output)