"""
Das requests - Package (http for humans)
https://github.com/psf/requests
"""

import requests


url = "https://google.de"
response = requests.get(url=url)
print(response)  # Response Objekt, <Response [200]>

# Status
print(response.status_code)

# Content
print(response.text[:39])
