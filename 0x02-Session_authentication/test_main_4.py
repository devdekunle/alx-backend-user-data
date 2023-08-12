#!/usr/bin/python3
""" Check response
"""
import requests

if __name__ == "__main__":
    cookie_value_send = "Holberton School"
    r = requests.get('http://0.0.0.0:5000/', cookies={'_cookie_cookie_dough': cookie_value_send})
    if r.status_code != 200:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    if r.headers.get('content-type') != "application/json":
        print("Wrong content type: {}".format(r.headers.get('content-type')))
        exit(1)
    
    try:
        r_json = r.json()
        
        cookie_value = r_json.get('cookie')
        if cookie_value is None:
            print("Request should contain a cookie")
            exit(1)

        if cookie_value_send != cookie_value:
            print("Cookie are different: {} != {}".format(cookie_value, cookie_value_send))
            exit(1)
            
        print("OK", end="")
    except:
        print("Error, not a JSON")
