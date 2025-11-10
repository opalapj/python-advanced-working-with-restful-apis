import json

import requests
from utils import crud
from utils import make_url
from utils import show_data
from utils import show_headers


# url = make_url()
# url = make_url(item=8)
# url = make_url(query={'_limit': 3, '_page': 1})
# url = make_url(query={'_sort': ['convertible', 'production_year'], '_order': ['asc', 'desc'], '_limit': 3, '_page': 2})

NEW = {
    "id": "4",
    "brand": "Volvo",
    "model": "V60",
    "production_year": 2016,
    "convertible": False,
}

REVISED = {
    "brand": "Volvo",
    "model": "V60",
    "production_year": 1999,
    "convertible": True,
}

try:
    # r = crud(make_url(resource='foo'), close_conn=True)
    # r = crud(make_url(resource='foo'))
    # r = crud(make_url(resource='foo'), 'c', NEW)
    # r = crud(make_url(resource='foo'), 'r')
    # r = crud(make_url(resource='foo', item=69), 'u', REVISED)
    r = crud(make_url(resource="foo", item=6), "d")
except requests.RequestException:
    print("Communication error")
else:
    show_headers(r)
    if r.ok:
        if r.request.method == "GET":
            cars = r.json()  # Using the requests package.
            # cars = json.loads(r.text)  # Using the json module.
            show_data(cars)
    elif r.status_code == requests.codes.NOT_FOUND:
        print(
            "The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible."
        )
    elif r.status_code == requests.codes.BAD_REQUEST:
        print(
            "The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing)."
        )
    else:
        print("Server error")
        print("Status code:", r.status_code)
        print(r.text)
finally:
    print("The work is done.")
