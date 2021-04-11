import json
from typing import Mapping

json_data = { 
    "results": [ 
        { 
        "location": { 
        "id": "WX4FBXXFKE4F", 
        "name": "北京", 
        "country": "CN", 
        "path": "北京,北京", 
        "timezone": "Asia/Shanghai", 
        "timezone_offset": "+08:00" 
            } 
        } 
    ] 
}

b = json.dumps(json_data)

print(b, type(b))

c = json.loads(b)

print(c, type(c))