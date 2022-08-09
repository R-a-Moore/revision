import requests # imports the requests package (with installation) which is needed to run api in this example

response = requests.get("https://en.wikipedia.org/wiki/API") # creates an instance of the request response, in this case calling the Wikipedia page for APIs
print(response.status_code) # prints the HTTP response code; 200 being a healthy response
print(response.text) # prints the json file text/content of the request response
