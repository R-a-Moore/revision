# Revision
## codewars tasks

### take in a sentence and reverse every word in it which is 5 or more characters long
```commandline
def spin_words(sentence): # take in a sentence and reverse every word in it which is 5 or more characters long
    return_sentence = "" # empty manipulator sentence
    for word in sentence.split(): # iterates through original sentence which is divided into words (removes all spaces however)
        if len(word) >= 5: # checks if word is 5 characters or more
            return_sentence += ''.join(reversed(word)) + " " # reverses word and injects it into empty sentence, also automatically injects space
        else:
            return_sentence += word + " " # injects word less than 5 characters into sentence without reversing, also automatically injects space
    return return_sentence[:-1] # returns resultant sentence, removing the last space from it
```

### square every digit of a number and concatenate them.
```commandline
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
```

### Return the number (count) of vowels in the given string
```commandline
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
def getCount(s):
    return sum(c in 'aeiou' for c in s) # gets the sum of the True returns for whether each letter in the inputed string (s) exists within the 'aeiou' string
```

## APIs
### What is an API?
Application Programming Interface (API), a way for two or more programs to interact with oneanother. It is a type of interface, offering a service to other pieces of software.
Documentation detailing connections over API software is called API specification. A computer which meets these standards is said to implement or expose  an API.

APIs architecture is typically viewed in a client-server relationship with the client sending the request for service and the server being the machine that provides response.

there are four different methodologies of APIs:
- SOAP (Simple Object Access Protocol). Client server messages are exchanged using XML. less flexible, more popular in the past.
- RPC (Remote Procedure Calls), client completes function/procedure on the server, and an output is responded with by the server.
- Wbsocket, modern web API that uses JSON. supports two way communication  between client & server. due to being able to send callback messages by the server to connected clients, its more efficient than REST.
- REST, most popular and flexible API found today on web. client sends requests as data. server uses this client input to begin internal functions, returning output data back to client.

Web APIs are software which communicates between client web-applications and the server.

APIs provide a layer of security. Provide direct service on a web-app is dangerous as it can be hacked. Sending it to an API which can handle sensitive data from clients and databases internally allows for encapsulation.

```commandline
import requests # imports the requests package (with installation) which is needed to run api in this example

response = requests.get("https://en.wikipedia.org/wiki/API") # creates an instance of the request response, in this case calling the Wikipedia page for APIs
print(response.status_code) # prints the HTTP response code; 200 being a healthy response
print(response.text) # prints the json file text/content of the request response

```

