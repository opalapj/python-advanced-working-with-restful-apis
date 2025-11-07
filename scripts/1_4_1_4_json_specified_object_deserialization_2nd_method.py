import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, e):
        print("In redefined default method. Object type:", type(e))
        if isinstance(e, Who):
            print("Serialization possible.")
            return e.__dict__
        else:
            print("Serialization is not possible.")
            return (
                "Object type is not supported."  # 1st - returning of serializable info.
            )
            # return super().default(e)  # 2nd - returning of defualt encoding (to raise a TypeError).


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_who)

    @staticmethod
    def decode_who(d):
        if list(d.keys()) == ["name", "age"]:
            return Who(**d)
        else:
            return d


some_man = Who("John Doe", 42)

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
]

encoded_python_objects = []
for o in python_objects_to_encoding:
    encoded_python_object = json.dumps(o, cls=MyEncoder)
    encoded_python_objects.append(encoded_python_object)

json_objects_to_decoding = encoded_python_objects
decoded_json_objects = []
for o in json_objects_to_decoding:
    decoded_json_object = json.loads(o, cls=MyDecoder)
    decoded_json_objects.append(decoded_json_object)

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
