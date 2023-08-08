import json
import requests
from time import sleep
from urllib.request import Request, urlopen

# Discord webhook URL
WEBHOOK_URL = "WEBHOOK_URL"

# Headers for API requests
WEBHOOK_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}

# JSON payload for sending a message
payload = json.dumps({"content": "Message"})

# API endpoint for fetching dad jokes
url = "https://dad-jokes.p.rapidapi.com/random/joke"

# Headers for dad jokes API
headers = {
    "X-RapidAPI-Key": "X-RapidAPI-Key",
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

# Send a GET request to the dad jokes API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    success = data["success"]
    body = data["body"]
    
    if success and body:
        joke = body[0]
        _id = joke["_id"]
        joke_type = joke["type"]
        setup = joke["setup"]
        punchline = joke["punchline"]
        
        # Print joke details
        print("ID:", _id)
        print("Type:", joke_type)
        print("Setup:", setup)
        print("Punchline:", punchline)
    else:
        print("No joke found in the response.")
else:
    print("Error:", response.status_code)

try:
    # Send setup part of the joke to Discord webhook
    payload = json.dumps({"content": setup})
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=WEBHOOK_HEADERS)
    urlopen(req)
    
    # Sleep for 10 seconds before sending the punchline
    sleep(10)
    
    # Send punchline part of the joke to Discord webhook
    payload = json.dumps({"content": punchline})
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=WEBHOOK_HEADERS)
    urlopen(req)
except:
    print("ERROR: Couldn't send message.")
