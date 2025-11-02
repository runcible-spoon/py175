import re

path_and_params = '/?rolls=2&sides=6'

path = re.search(r'\/[^?]*', path_and_params)
params = re.search(r'\?.*', path_and_params)

# path, params = re.match(r'\/[^?]*\?', path_and_params), re.match(r'^\?.*', path_and_params)

print(path[0], params[0])
