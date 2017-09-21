##client file

import settings
from requests import *
from threading import Thread

def light_status():
    url="https://tautomator.herokuapp.com/stream/240cfd9667f64791ac2062ff690d2024"
    r=get(url)
    data=r.json()
    return data

def fan_status():
    url="https://tautomator.herokuapp.com/stream/cb533527dccb4e9eb84079588b342d63"
    r=get(url)
    data=r.json()
    return data


def tv_status():
    url="https://tautomator.herokuapp.com/stream/cb533527dccb4e9eb84079588b342d65"
    r=get(url)
    data=r.json()
    return data


if __name__ =='__main__':
    while True:
        t1=light=light_status()['state']
        fan=fan_status()['state']
        tv=tv_status()['state']
        print("light is >> {0}".format(light))
        print("fan is >> {0}".format(fan))
        print("tv is >> {0}".format(tv))
        ###your code here binil
