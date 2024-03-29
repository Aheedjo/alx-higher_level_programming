#!/usr/bin/python3
"""
a script that sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":
    import sys
    import requests

    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
