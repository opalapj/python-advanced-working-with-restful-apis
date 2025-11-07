import json


python_float = 1.602176620898e10
json_float = json.dumps(python_float)
print(python_float)
print(json_float)

python_str = '"The Meaning of Life" by Monty Python\'s Flying Circus'
json_str = json.dumps(python_str)
print(python_str)
print(json_str)

python_list = [1, 2.34, True, False, "False", None, ["a", 0]]
json_list = json.dumps(python_list)
print(python_list)
print(json_list)

python_dict = {"me": "Python", "pi": 3.1415, "data": (1, 2, 3), "set": None}
json_dict = json.dumps(python_dict)
print(python_dict)
print(json_dict)

# Possible ways of serializing and deserializing Python and JSON objects.
python_object_w = {
    "str": "something",
    "float": 3.1415,
    "int": 3,
    "tuple": (1, 2, 3),
    "list": [1, 2, 3],
    "dict": {"a": 1, "b": 2, "c": 3},
    "true": True,
    "false": False,
    "none": None,
    "empty": {},
}
# Serialize (encode) Python obj to a JSON formatted string.
json_object = json.dumps(python_object_w)

# Deserialize (decode) JSON formatted string to a Python object.
python_object_r0 = json.loads(json_object)

print(python_object_w)
print(python_object_r0)

# Serialize (encode) Python obj as a JSON formatted stream
# to a .write()-supporting file-like object.
with open("data/json_object.txt", mode="w") as stream:
    json.dump(python_object_w, stream)

# Deserialize (decode) a .read()-supporting text file or binary file
# containing a JSON document to a Python object.
with open("data/json_object.txt", mode="r") as stream:
    python_object_r1 = json.load(stream)

print(python_object_w)
print(python_object_r1)
