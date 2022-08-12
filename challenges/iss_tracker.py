#!/usr/bin/env python3

#request module
import requests

#define url function
URL = "http://api.open-notify.org/iss-now.json"

def main():
    response = requests.get(URL).json()

    if _name_ == "_main":
        main()


