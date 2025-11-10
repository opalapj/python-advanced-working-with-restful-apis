import requests


r = requests.request(
    method="get",
    url="http://localhost:3000/cars",
    # url='http://localhost:3000',
)

# Status codes.
for status, code in requests.codes.__dict__.items():
    print(f"{status} -> {code}")

code = 201
print(dict(filter(lambda x: x[1] == code, requests.codes.__dict__.items())))

print(r.status_code)

if r.status_code == requests.codes.OK:
    print(":)")

# Headers.
for header, value in r.request.headers.items():
    print(header, "->", value)

for header, value in r.headers.items():
    print(header, "->", value)

# Content.
print(r.text)  # String.
print(r.content)  # Text.
