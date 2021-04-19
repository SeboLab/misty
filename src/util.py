import re
import time
import subprocess as sp

import requests


def ping_ip(ip, timeout):
    """Continuously ping an IP until a timeout period.

    Returns True if the IP is up within that duration
    """
    ping_cmd = "ping -c 1 -w 1".split(" ")
    ping_cmd.append(ip)
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            response = sp.run(
                ping_cmd, timeout=timeout, stdout=sp.PIPE, stderr=sp.PIPE, check=True
            )
            if "1 received" in str(response.stdout):
                return True
        except sp.TimeoutExpired:
            continue
    return False


def ros_msg_to_json(msg):
    json = dict()
    for field in dir(msg):
        if field.startswith("_") or "serialize" in field:
            continue

        words = [word.capitalize() for word in field.split("_")]
        camel_case_field = "".join(words)

        json[camel_case_field] = getattr(msg, field)
    return json


def json_to_ros_msg(json_obj):
    msg = {}
    for attr in dir(json_obj):
        msg[re.sub("(?<!^)(?=[A-Z])", "_", attr).lower()] = json_obj[attr]
    return msg


def post(ip, endpoint, json=None):
    if json is None:
        return requests.post("http://" + ip + "/api/" + endpoint)
    else:
        return requests.post("http://" + ip + "/api/" + endpoint, json=json)


def get(ip, endpoint, json=None):
    if json is None:
        return requests.get("http://" + ip + "/api/" + endpoint)
    else:
        return requests.get("http://" + ip + "/api/" + endpoint, json=json)


def delete(ip, endpoint, json):
    return requests.delete("http://" + ip + "/api/" + endpoint, json=json)
