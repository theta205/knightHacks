import requests
import json

def photoAPI(input):
    url = "https://api.serphouse.com/serp/live"

    payload = {
        "data": {
            "q": input,
            "domain": "google.com",
            "loc": "Orlando,Florida,United States",
            "lang": "en",
            "device": "desktop",
            "serp_type": "image",
            "page": "1",
            "verbatim": "0",
        }
    }

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': "Bearer dZJd4JQ1aTjYvzvfLD8eh1l8tCCmHhuB2r5fdEMM02Ybh35bszkqSOCDnogB"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Check if the response has a JSON content type
    if response.headers.get('content-type') == 'application/json':
        # Parse the JSON response
        json_response = response.json()
        # Pretty print the JSON
        for value in json_response['results']['results']:
            original_url = value['original']
            if original_url.endswith('.jpg') or original_url.endswith('.png') or original_url.endswith('.jpeg'):
                print(original_url)
                break  # Exit the loop after the first valid URL

photoAPI("Dyson V11") # change if needed
