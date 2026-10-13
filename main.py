
import requests

url = "https://httpbin.org/get"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    print("Status code:", response.status_code)
    print("Website:", response.json()["url"])

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
