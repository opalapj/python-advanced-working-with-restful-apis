import json


# cmd -> python <file_name>


class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

    @classmethod
    def user_creation(cls):
        rn = input("Registration number: ")
        yop = int(input("Year of production: "))
        p = input("Passenger [y/n]: ").upper() == "Y"
        m = float(input("Vehicle mass: "))
        return cls(rn, yop, p, m)


class MyEncoder(json.JSONEncoder):
    def default(self, unknown):
        if isinstance(unknown, Vehicle):
            return unknown.__dict__
        else:
            return super().default(unknown)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_vehicle)

    @staticmethod
    def decode_vehicle(dic):
        if list(dic.keys()) == [
            "registration_number",
            "year_of_production",
            "passenger",
            "mass",
        ]:
            return Vehicle(**dic)
        else:
            return dic


print(
    """What can I do for you?
1 - produce a JSON string describing a vehicle
2 - decode a JSON string into a vehicle data"""
)
while True:
    mode = input("Your choice: ")
    if mode == "1":
        # vehicle = Vehicle('WP7023F', 2008, 'y', 1650)
        vehicle = Vehicle.user_creation()
        json_string = json.dumps(vehicle, cls=MyEncoder)
        print("Resulting JSON string is:\n{}".format(json_string))
        break
    elif mode == "2":
        # json_string = '{"registration_number": "w", "year_of_production": "2", "passenger": true, "mass": "1"}'
        json_string = input("Enter vehicle JSON string: ")
        vehicle = json.loads(json_string, cls=MyDecoder)
        print("{}".format(vehicle.__dict__))
        break
    else:
        print("Wrong choice, try again.")
print("Done")
