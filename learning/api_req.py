#!/usr/bin/env python3

#a simple exploration of creating a request to an api
#and inserting my own data into the received json

import requests
import json
res = requests.get("https://api.sunrise-sunset.org/json")
print("Received JSON:")
print(json.dumps(res.json(), indent=3))
new_dict = {"test": {"it1": "msg1", "it2": "msg2", "it3": "msg3"}}
res = list(res.json().items())
out = {}
out.update(res[:1])
out.update(new_dict)
out.update(res[1:])
print("\nModified JSON:")
print(json.dumps(out, indent=3))
