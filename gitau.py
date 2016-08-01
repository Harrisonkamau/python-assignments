"""
This is a Python Snippet that filters data in a JSON file based on the gender the user inputs
It then outputs the number per each gender
"""

import json
# user_input = int(raw_input("Enter id:  "))

with open('gitau.json')as json_data:
    data = json.load(json_data)
    for item in range(len(data)):
        print item




