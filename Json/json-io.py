import json


req = {
        "move": {
            "advance": True,
            "left": False,
            "right": False,
            "back": False
            }
        }

jsonStr = json.dumps(req)

print(jsonStr)

jsonObj = json.loads(jsonStr)

print(jsonObj)
print(jsonObj["move"])
print(jsonObj["move"]["advance"])
print(jsonObj["move"]["left"])
print(jsonObj["move"]["right"])
print(jsonObj["move"]["back"])
