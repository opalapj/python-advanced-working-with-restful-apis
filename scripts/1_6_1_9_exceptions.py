import requests


# requests.exceptions.Timeout - we agree to wait for a server's response.
# If the time is exceeded, get() will raise an exception.
try:
    response = requests.request(method="get", url="http://localhost:3000", timeout=1)
except requests.exceptions.Timeout:
    print("Sorry, Mr. Impatient, you didn't get your data")
else:
    print("Here is your data, my Master!")

# requests.exceptions.ConnectionError - problems may appear much earlier,
# e.g., while establishing the connection.
try:
    response = requests.request(method="get", url="http://localhost:3001", timeout=1)
except requests.exceptions.ConnectionError:
    print("Nobody's home, sorry!")
else:
    print("Everything fine!")

# requests.exceptions.InvalidURL -  it is also possible that you or another
# developer may leave the resource’s URI in a somewhat malformed state.
try:
    response = requests.request(method="get", url="http:////////////")
except requests.exceptions.InvalidURL:
    print("Recipient unknown!")
else:
    print("Everything fine!")
