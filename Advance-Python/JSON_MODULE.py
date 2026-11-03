## JSON ==> JAVA SCRIPT OBJECT NOTATION
## python has a inbuilt json module to work with json data

import json

## Convert(Parse) json to python: To perform this operation we use loads()

x  = '{"name":"steve", "age":23, "city":"Bangalore"}'
print(type(x))

## Convert(Parse) to python
x = json.loads(x)
print(type(x))

###################################################################################

## Convert(Parse) python to json: To perform this operation we use dumps()

x = {"name":"steve", "age":23, "city":"Bangalore"}
print(type(x))

## Convert(Parse) to json
x = json.dumps(x)
print(type(x))

##################################################################################

## when we convert the python to json or json to python it converts the datatype as well

# Python	        JSON
# dict	        Object/map
# list	        Array
# tuple	        Array
# str	        String
# int	        Number
# float	        Number
# True	        true
# False	        false
# None	        null

x = {
  "name": "steve",
  "age": 40,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
# print(json.dumps(x, indent=4))
# print(json.dumps(x, indent=4, sort_keys=True))


## Writing the python data into the json file: To perform this operation we use dump()

x = {
  "name": "steve",
  "age": 40,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

with open('sample.json', 'w') as a:
    json.dump(x, a, indent=5, sort_keys=True)


###############################################################################

## Reading the data from the json file: To perform this operation we use load()

with open('sample.json', 'r') as a:
    print(json.load(a))

