import json
x = '{"name":"John", "age":30, "Class":"SS1"}'
y = json.loads(x)
print(y["Class"])
print(y)

