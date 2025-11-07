import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Who1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(e):
    print("In redefined default function. Object type:", type(e))
    if isinstance(e, Who):
        print("Serialization possible.")
        return e.__dict__
    else:
        print("Serialization is not possible.")
        return "Object type is not supported."  # 1st - returning of serializable info.
        # return json.JSONEncoder().default(e)  #  2nd - returning of defualt encoding (to raise a TypeError).


def decode_who(w):
    # return Who(w['name'], w['age'])
    return Who(**w)  # More professional way to encapsulate keyword args.


some_man = Who("John Doe", 42)
other_man = Who1("Roman Opala", 60)

python_objects_to_encoding = [
    "a",
    2,
    3.0,
    [1, 2, 3],
    {"a": 1, "b": 3, "c": 3},
    True,
    None,
    some_man,
    {"name": "Piotr Opala", "age": 29},
    other_man,
]

encoded_python_objects = []
for o in python_objects_to_encoding:
    json_object = json.dumps(o, default=encode_who)
    encoded_python_objects.append(json_object)

json_objects_to_decoding = encoded_python_objects
for o in json_objects_to_decoding:
    decoded_json_object = json.loads(o, object_hook=decode_who)

# How .loads method works:
# Checking all parameters.
#   If defaults - run json.JSONDecoder().decode() decoder.
#   If not - checking if cls parameter (decoder) was redefined.
#     If was - initiate cls() decoder and run .decode() method with defined parameters.
#       Method uses object_hook parameter to choose way of decoding json object.
#         If none - run built-in function decode json object to python dict.
#         If not (redefined) - run redefined function.
#     If was not - initiate json.JSONEncoder() encoder and run .encode() method with defined parameters.
#       Method uses object_hook parameter to choose way of decoding json object.
#         If none - run built-in function decode json object to python dict.
#         If not (redefined) - run redefined function.
