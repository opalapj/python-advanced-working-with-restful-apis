import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


python_object = {
    "a": "a",
    2: 2,
    3.0: 3.0,
    True: True,
    None: None,
    Who: "illegal key type",  # TypeError: keys must be str, int, float, bool or None, not type
}

json_object = json.dumps(
    python_object,
    skipkeys=True,  # Skip key with not a basic type instead of raising a TypeError.
)

print(json_object)
