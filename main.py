import requests
from connecting import config


if __name__ == "__main__":
    a = config()
    req = requests.get("https://docs.google.com/spreadsheets/d/1tI_cYNmUkvE58a1X74hh9IlapfiGeMTfuNU7AVGCajU/")
    print(a, req, sep = "\n")
    req.json()
