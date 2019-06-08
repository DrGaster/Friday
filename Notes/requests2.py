# importing the requests library 
import requests
import pprint
# api-endpoint 
URL = "https://swapi.co/api/people/1"

# location given here 
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location}

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format 
data = r.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)