# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:28:26 2024

@author: debkumar
"""

import json

"""
Following code dempnstrates json.dumps() and json.loads() functionalities
"""
json_string = '''{
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}
'''

data = json.loads(json_string)
print(data['quiz']['sport']['q1']['options'])

#removing last option

del data['quiz']['sport']['q1']['options'][3]

print(data['quiz']['sport']['q1']['options'])

new_json_string = json.dumps(data, indent =2, sort_keys= False)

print(new_json_string)


"""
Following code dempnstrates json.dumps() and json.loads() functionalities
"""

with open("sample_json.json","r") as f:
    json_string_from_file = json.load(f)
    
addresses= json_string_from_file['Policy']["Address"]

#write a addresses to a jsonfile.

with open("address.json","w") as f:
    json.dump(addresses, f, indent=2)
   
