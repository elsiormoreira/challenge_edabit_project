"""
Create a function that takes a dictionary
as an argument and returns a string with
facts about the city. The city facts will
need to be extracted from the dictionaries
three properties:

1. name
2. population
3. continent

The string should have the following format:
X has a population of Y and is situated in Z
(where X is the city name, Y is the population
and Z is the continent the city is situated in).

Examples
city_facts({
  name: "Paris",
  population: "2,140,526",
  continent: "Europe"
    }) ➞ "Paris has a population of 2,140,526 and is situated in Europe"

city_facts({
  name: "Tokyo",
  population: "13,929,286",
  continent: "Asia"
}) ➞ "Tokyo has a population of 13,929,286 and is situated in Asia"

"""

# my solution
def city_facts(city):
    return '{} has a population of {} and is situated in {}'.format(city['name'], city['population'], city['continent'])
