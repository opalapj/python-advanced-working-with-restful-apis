import json

import requests


def check_server(car_id=None):
    uri_check = uri if car_id is None else "/".join([uri, str(car_id)])
    response = requests.head(uri_check, headers=connection)
    if response.status_code == requests.codes.ok:
        return True
    elif response.status_code == requests.codes.not_found:
        return False


def print_menu():
    print("+-----------------------+")
    print("| Vintage Cars Database |")
    print("+-----------------------+")
    print("MENU")
    print("1. List cars")
    print("2. Add car")
    print("3. Delete car")
    print("4. Update car")
    print("5. Exit")


def read_user_choice():
    while True:
        mode = input("Enter your choice (1-5): ")
        if mode in ["1", "2", "3", "4", "5"]:
            return mode
        else:
            print("Try again.")


def print_header():
    for attribute, column_width in zip(attributes, column_widths):
        print(attribute.ljust(column_width), end="| ")
    print()


def print_car(car):
    for attribute, column_width in zip(attributes, column_widths):
        print(str(car[attribute]).ljust(column_width), end="| ")
    print()


def name_is_valid(name):
    parts = list(filter(lambda x: x.isalnum(), name.split()))
    return bool(parts)


def enter_id():
    while True:
        car_id = input("Car ID (empty string to exit): ")
        if car_id:
            try:
                car_id = int(car_id)
                if car_id < 0:
                    raise ValueError
                else:
                    return car_id
            except ValueError:
                print("Valid car ID consist digits only. Try again.")
        else:
            return


def enter_production_year():
    while True:
        car_year = input("Car production year (empty string to exit): ")
        if car_year:
            try:
                car_year = int(car_year)
                if 1900 <= car_year <= 2000:
                    return car_year
                else:
                    raise ValueError
            except ValueError:
                print(
                    "Valid production year is an int from range 1900..2000. Try again."
                )
        else:
            return


def enter_name(attribute):
    while True:
        instruction = "Car {} (empty string to exit): ".format(attribute)
        car_name = input(instruction)
        if car_name:
            if name_is_valid(car_name):
                return car_name.strip()
            else:
                print(
                    "Valid name is non-empty string containing digits, letters and spaces. Try again."
                )
        else:
            return


def enter_convertible():
    while True:
        car_convertible = input(
            "Is this car convertible? [y/n] (empty string to exit): "
        ).upper()
        if car_convertible:
            if car_convertible in ["Y", "N"]:
                return car_convertible == "Y"
            else:
                print("Valid answer is yes or no [y/n]. Try again.")
        else:
            return


def input_car_data(with_id):
    car_data = {}
    if with_id:
        car_id = enter_id()
        if car_id is None:
            return
        else:
            car_data[attributes[0]] = car_id
    car_brand = enter_name("brand")
    if car_brand is None:
        return
    else:
        car_data[attributes[1]] = car_brand
    car_model = enter_name("model")
    if car_model is None:
        return
    else:
        car_data[attributes[2]] = car_model
    car_year = enter_production_year()
    if car_year is None:
        return
    else:
        car_data[attributes[3]] = car_year
    car_convertible = enter_convertible()
    if car_convertible is None:
        return
    else:
        car_data[attributes[4]] = car_convertible
    return car_data


def list_cars():
    response = requests.get(uri, headers=connection)
    cars = response.json()
    if cars:
        print_header()
        for car in cars:
            print_car(car)
    else:
        print("Database is empty.")


def add_car():
    car_data = input_car_data(True)
    if car_data:
        requests.post(uri, headers=content, data=json.dumps(car_data))
        print("Success!")
    else:
        print("Adding aborted.")


def delete_car():
    car_id = enter_id()
    if car_id:
        if check_server(car_id):
            requests.delete("/".join([uri, str(car_id)]))
            print("Success!")
        else:
            print("Car ID not found.")
    else:
        print("Deleting aborted.")


def update_car():
    car_id = enter_id()
    if car_id:
        if check_server(car_id):
            car_data = input_car_data(False)
            if car_data:
                requests.put(
                    "/".join([uri, str(car_id)]),
                    headers=content,
                    data=json.dumps(car_data),
                )
                print("Success!")
            else:
                print("Updating aborted.")
        else:
            print("Car ID not found.")
    else:
        print("Updating aborted.")


attributes = ["id", "brand", "model", "production_year", "convertible"]
column_widths = [5, 16, 16, 16, 16]
uri = "http://localhost:3000/cars"
content = {"Content-Type": "application/json"}
connection = {"Connection": "close"}
while True:
    if not check_server():
        print("Server is not responding - quitting!")
        break
    print_menu()
    choice = read_user_choice()
    if choice == "1":
        list_cars()
    elif choice == "2":
        add_car()
    elif choice == "3":
        delete_car()
    elif choice == "4":
        update_car()
    elif choice == "5":
        print("Bye!")
        break
