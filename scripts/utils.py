import json
import urllib.parse

import requests


# urllib.parse.urlparse('http://localhost:3000/cars')
# ParseResult(scheme='http', netloc='localhost:3000', path='/cars', params='', query='', fragment='')

# urllib.parse.urlparse('http://localhost:3000/cars/2')
# ParseResult(scheme='http', netloc='localhost:3000', path='/cars/2', params='', query='', fragment='')

# urllib.parse.urlparse('http://localhost:3000/cars?_sort=production_year&_order=desc')
# ParseResult(scheme='http', netloc='localhost:3000', path='/cars', params='', query='_sort=production_year&_order=desc', fragment='')

# urllib.parse.parse_qs('_sort=production_year&_order=desc')
# {'_sort': ['production_year'], '_order': ['desc']}

# urllib.parse.parse_qsl('_sort=production_year&_order=desc')
# [('_sort', 'production_year'), ('_order', 'desc')]

# urllib.parse.parse_qs('_sort=convertible%2Cproduction_year&_order=asc%2Cdesc')
# {'_sort': ['production_year'], '_order': ['desc']}

# urllib.parse.parse_qsl('_sort=convertible%2Cproduction_year&_order=asc%2Cdesc')
# [('_sort', 'production_year'), ('_order', 'desc')]

HEADERS = {"id": 10, "brand": 15, "model": 10, "production_year": 20, "convertible": 15}


def make_query(query):
    if query is None:
        return {}
    else:
        query_tmp = {}
        for key, value in query.items():
            if isinstance(value, list):
                value = ",".join(value)
            query_tmp[key] = value
        return urllib.parse.urlencode(query_tmp)


def make_url(
    scheme=None,
    hostname=None,
    port=None,
    resource=None,
    item=None,
    params=None,
    query=None,
    fragment=None,
):
    scheme = scheme or "http"
    hostname = hostname or "localhost"
    port = port or 3000
    resource = resource or "cars"
    item = item or ""
    netloc = ":".join([hostname, str(port)])
    path = "/".join([resource, str(item)])
    query = make_query(query)
    parts = (scheme, netloc, path, params, query, fragment)
    return urllib.parse.urlunparse(parts)


def show_resource_headers():
    for n, w in HEADERS.items():
        print(n.ljust(w), end="| ")
    print()


def show_empty():
    for w in HEADERS.values():
        print(" ".ljust(w), end="| ")
    print()


def show_item(item):
    for n, w in HEADERS.items():
        print(str(item[n]).ljust(w), end="| ")
    print()


def show_data(items):
    show_resource_headers()
    if type(items) is list:
        for car in items:
            show_item(car)
    elif type(items) is dict:
        if items:
            show_item(items)
        else:
            show_empty()
    print()


def show_headers(response):
    print("Request headers:")
    for header, value in response.request.headers.items():
        print(header, ":", value)
    print()
    print("Response headers:")
    for header, value in response.headers.items():
        print(header, ":", value)
    print()


def choose_method(activity):
    activity = activity.upper()
    if activity == "C":
        return "POST"
    elif activity == "R":
        return "GET"
    elif activity == "U":
        return "PUT"
    elif activity == "D":
        return "DELETE"


def crud(url, activity=None, data=None, close_conn=False):
    kwargs = {"url": url}
    headers = {}
    if activity is None:
        method = "HEAD"
    else:
        method = choose_method(activity)
    kwargs["method"] = method
    if method in ["POST", "PUT"]:
        # headers['Content-Type'] = 'application/json'
        # headers['Content-Type'] = 'application/vnd.api+json'  # For tests.
        # kwargs['data'] = json.dumps(data)  # Using the json module.
        kwargs["json"] = (
            data  # Using the requests package - serialization of python object and setting of application/json header are done automatically.
        )
    if close_conn:
        headers["Connection"] = "close"
    if headers:
        kwargs["headers"] = headers
    return requests.request(**kwargs)


if __name__ == "__main__":
    print(make_url())
    print(make_url(resource="cars"))
    print(make_url(resource="cars", item=2))
    print(
        make_url(resource="cars", query={"_sort": "production_year", "_order": "desc"})
    )
    print(
        make_url(
            resource="cars", query={"_sort": ["production_year"], "_order": ["desc"]}
        )
    )
    print(
        make_url(
            resource="cars",
            query={
                "_sort": ["convertible", "production_year"],
                "_order": ["asc", "desc"],
            },
        )
    )
    print(make_url(resource="cars", query={"_limit": 3}))
    print(make_url(resource="cars", query={"_limit": 3, "_page": 1}))
    print(
        make_url(
            resource="cars",
            query={
                "_sort": ["convertible", "production_year"],
                "_order": ["asc", "desc"],
                "_limit": 3,
                "_page": 1,
            },
        )
    )

    show_data(
        {
            "id": "4",
            "brand": "Volvo",
            "model": "V60",
            "production_year": 2016,
            "convertible": False,
        }
    )
    show_data(
        [
            {
                "id": "4",
                "brand": "Volvo",
                "model": "V60",
                "production_year": 2016,
                "convertible": False,
            },
            {
                "brand": "Volvo",
                "model": "V60",
                "production_year": 1999,
                "convertible": True,
            },
        ]
    )
